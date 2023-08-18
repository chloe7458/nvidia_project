#!/usr/bin/python3

# the contents of this file will be copied to duckImagenet.py (the main file) periodically as I work
# this file will be removed when the project is complete
# for now this file is for experimentation I think

from jetson_inference import imageNet
from jetson_utils import videoSource, videoOutput, cudaFont, Log

import sys
import argparse


# parse the command line
parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="googlenet", help="model to use, can be:  googlenet, resnet-18, etc. (see --help for others)")

try:
	args = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)


# load the recognition network
net = imageNet(args.network, sys.argv)


# create video sources and outputs
input = videoSource(args.input, argv=sys.argv)
output = videoOutput(args.output, argv=sys.argv)
class_font = cudaFont(size=30)
advice_font = cudaFont(size=20)


# process frames until EOS or the user exits
while True:
    # capture the next image
    img = input.Capture()
    
    if img is None: # timeout
        continue  
        
    # classify the image and get the top class information
    class_id, confidence = net.Classify(img)
    class_desc = net.GetClassDesc(class_id)
    class_label = net.GetClassLabel(class_id)

    confidence *= 100

    # print top class prediction
    print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_id, confidence))

    # give advice
    if class_desc.find("beaver"):
        class_label = "beaver"
    else:
        advice = "i am thinking ..."
    
    # draw top class label
    class_font.OverlayText(img, text=f"{confidence:05.2f}% {class_label}", 
                     x=5, y=5,
                     color=class_font.White, background=class_font.Gray40)

    # draw advice label
    advice_font.OverlayText(img, text=str(advice), 
                     x=5, y=35,
                     color=advice_font.White, background=advice_font.Gray40)

    # render the image
    output.Render(img)
    
    # update the title bar
    output.SetStatus("{:s} | Network {:.0f} FPS".format(net.GetNetworkName(), net.GetNetworkFPS()))

    # print out performance info
    #net.PrintProfilerTimes()

    # exit on input/output EOS
    if not input.IsStreaming() or not output.IsStreaming():
        break
