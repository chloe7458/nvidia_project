#!/usr/bin/python3

from jetson_inference import imageNet
from jetson_utils import videoSource, videoOutput, cudaFont, Log

import sys
import os

import argparse


# parse the command line
parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output", type=str, default="", nargs='?', help="URI of the output stream")

try:
	args = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)


# load the recognition network
net = imageNet(model="/home/nvidia/jetson-inference/python/training/classification/models/pond/resnet18.onnx",
                 labels="/home/nvidia/jetson-inference/python/training/classification/models/pond/labels.txt", 
                 input_blob="input_0", output_blob="output_0")


# create video sources and outputs
input = videoSource(args.input, argv=sys.argv)
output = videoOutput(args.output, argv=sys.argv)


# delete previous outputs
dir = "/home/nvidia/pond/output"
for file_path in os.listdir(dir):
    print("removed previous output",str(file_path))
    os.remove(os.path.join(dir,file_path))


# create fonts for overlay
class_font = cudaFont(size=30)
advice_font = cudaFont(size=15)


# process frames until EOS or the user exits
while True:
    # capture the next image
    img = input.Capture()
    
    if img == None: # timeout
        continue
        
    # classify the image and get the top class information
    class_id, confidence = net.Classify(img)
    class_desc = net.GetClassDesc(class_id)
    class_label = net.GetClassLabel(class_id)

    confidence *= 100

    # print top class prediction
    print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_id, confidence))

    # give advice
    class_list = ["beaver","duck","fish","frog","goose","heron","turtle"]
    advice_list = ["vegetables",
                    "corn, oats, rice, seeds",
                    "algae, plants, bugs, fish",
                    "worms and insects",
                    "grass, seeds, grain, fruits",
                    "squirrels, fish",
                    "fruits, bugs, fish"]

    advice_label = "something went wrong"

    for index in range(len(class_list)-1):
        class_name = class_list[index]

        if class_desc == class_name:
            advice_label = advice_list[index]
    
    # draw top class label
    class_font.OverlayText(img, text=f"{confidence:05.2f}% {class_label}", 
                     x=5, y=5,
                     color=class_font.White, background=class_font.Gray40)

    # draw advice label
    advice_font.OverlayText(img, text=str(advice_label), 
                     x=5, y=35,
                     color=advice_font.White, background=advice_font.Gray40)

    # render the image
    output.Render(img)
    
    # update the title bar
    output.SetStatus("{:s} | Network {:.0f} FPS".format(net.GetNetworkName(), net.GetNetworkFPS()))

    # print out performance info
    net.PrintProfilerTimes()

    # exit on input/output EOS
    if not input.IsStreaming() or not output.IsStreaming():
        break
