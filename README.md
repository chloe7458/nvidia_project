# Project Name

This project uses a resnet-18 network that is retrained to focus on recognizing different types of animals found near ponds: beavers, ducks, fish, frogs, herons, geese, and turtles. The model takes an image and classifies it as one of these seven animals, and then the algorithm creates a copy of the image with labels that show the animal's name and what the animal eats.

## The Algorithm

<details>
<summary>
   pond_imagenet.py
</summary>
   
1. Import the necessary modules.

   ![](https://i.ibb.co/hW1FKYF/Capture1.png)
   
2. Add input and output arguments in command line.

   ![](https://i.ibb.co/rGTbDNz/Capture2.png)
   
3. Define input and output from arguments.

   ![](https://i.ibb.co/dBtP658/Capture3.png)
   
4. Load the recognition network. This project uses resnet-18.

   ![](https://i.ibb.co/P1cJ7yF/Capture4.png)
   
5. (Optional) Delete previous outputs. Comment out these lines to keep previous outputs.

   ![](https://i.ibb.co/QCVCRwZ/Capture5.png)

6. Create fonts for overlay.

   ![](https://i.ibb.co/gg1kKQW/Capture6.png)
   
7. Capture the next image/frame.

   ![](https://i.ibb.co/PcTjwzt/Capture7.png)
   
8. Classify the image/frame using the recognition network.

   ![](https://i.ibb.co/5kPcqqD/Capture8.png)
   
9. Print the top class prediction.

   ![](https://i.ibb.co/gSxwjmS/Capture9.png)
   
10. Choose information on label depending on the class prediction.

    ![](https://i.ibb.co/DVfQgHK/Capture10.png)
    
11. Add the name and diet labels to the output image.

    ![](https://i.ibb.co/vqGs2kz/Capture11.png)
   
12. Render the output image.

    ![](https://i.ibb.co/2g50hSZ/Capture12.png)
    
</details>

## Running this project

1. Make sure the following are installed on your jetson nano: resnet-18, [jetson-inference](https://www.github.com/dusty-nv/jetson-inference/)
   
2. Connect to your jetson nano on VSCode.

   <details>
      <summary>SSH on VSCode</summary>
      
   1. Open VSCode and navigate to the Extensions tab.

         ![](https://i.ibb.co/hXR7yjK/Capture2bi.png)
      
   2. Install the Remote-SSH extension.
  
         ![](https://i.ibb.co/YfyYgnB/Capture2bii.png)
      
   3. Navigate to the Command Palette. (View > Command Palette or Ctrl + Shift + P)

         ![](https://i.ibb.co/8DFzD9h/Capture2biii.png)
      
   4. Select "Remote-SSH: Connect to Host..."
         
         ![](https://i.ibb.co/bbk0q3X/Capture2biv.png)
      
   5. Select "Add New SSH Host..."
       
         ![](https://i.ibb.co/n8yrD6C/Capture2bv.png)
      
   6. Type "nvidia@" followed by your jetson nano's IP address.
  
         ![](https://i.ibb.co/MSbVchx/Capture2bvi.png)
      
   7. Select the first option.
  
         ![](https://i.ibb.co/FBCFFqC/Capture2bvii.png)
      
   8. Connect to your jetson nano. If asked, select Linux as the platform for the remote host.
  
         ![](https://i.ibb.co/1X4P03v/tempsnip.png)
      
   9. Enter the password.
  
         ![](https://i.ibb.co/pv2t2xg/Capture2bxi.png)
          
   10. Select "Open Folder..." and enter "/home/".

          ![](https://i.ibb.co/4jXmZ5b/Capture2bxii.png)
   
   </details>

3. Download the [```data```](https://github.com/chloe7458/nvidia_project/tree/master/data) directory to your computer and move the contents into **/home/nvidia/jetson-inference/python/training/classification/data/**.

4. Create the directory **/home/nvidia/jetson-inference/python/training/classification/models/pond/** using ```mkdir``` or through the VSCode explorer.

5. Copy the [```labels.txt```](https://github.com/chloe7458/nvidia_project/blob/master/data/pond/labels.txt) file into **/home/nvidia/jetson-inference/python/training/classification/models/pond/**.
   
   Overall, the ```classification``` directory should look like this.

   ![](https://i.ibb.co/mCL7nfn/thing.png)

6. Open the terminal and navigate to **/home/nvidia/jetson-inference/**.

   ```
   $ cd nvidia/jetson-inference/
   ```

   ![](https://i.ibb.co/nQgqTwQ/6.png)
   
7. Open the docker container and enter the password.

   ```
   $ ./docker/run.sh
   ```
   
   ![](https://i.ibb.co/CPyswFp/7.png)
   
8. Navigate to **/jetson-inference/python/training/classification/** in the docker container.

   ```
   # cd python/training/classification/
   ```

   ![](https://i.ibb.co/YPBnG13/8.png)

9. Re-train the network using the data for this project. This will take some time.

   ```
   # python3 train.py --model-dir=models/pond/ data/pond/
   ```

10. Press ```Ctrl+C``` at any time to pause training.

    <details>
       <summary>Resuming training</summary>
      
       1. To resume training, run ```train.py``` with these parameters:
         
          ```
          # python3 train.py --resume models/pond/model_best.pth.tar --model-dir=models/pond data/pond
          ```
       
       2. If you get a silly error on line 196 about the best_accuracy variable, open ```train.py``` using this command.
          
          ```
          # nano train.py
          ``` 
          Look for these lines and comment them out, then save the file.
   
          https://github.com/chloe7458/nvidia_project/assets/55027449/093ea25c-b9a2-4649-9aae-46169428e134
         
          Try running the file again and it should work.

    </details>

11. Export the re-trained model using this command.

    ```
    # python3 onnx_export.py --model-dir=models/pond
    ```
    You should see the ONNX file in the explorer.

    ![](https://i.ibb.co/n3gVB8y/11.png)
  
12. When you are satisfied with the training, pause again and exit the docker container.

    ```
    # exit
    ```

    ![](https://i.ibb.co/KV7rfM2/12.png)
    
13. You should be back at **/home/nvidia/jetson-inference/**. Navigate to **/home/nvidia/pond/**.

    ```
    $ cd ..
    $ cd pond/
    ```

    ![](https://i.ibb.co/vHQgR5D/13.png)
    
14. To use the model, run ```pond_imagenet.py```.
    This command will make the model process all of the beaver images in the dataset for this project and saves the outputs to **/home/nvidia/pond/output/**.

    ```
    $ python3 pond_imagenet.py ../jetson-inference/python/training/classification/data/pond/test/beaver/"*.jpg" output/"output_%i.jpg"
    ```

    To process your own images, upload them to VSCode and change the file paths in the command.

15. Open the output files in VSCode to see the results.
   
    ![](https://i.ibb.co/m8LW6vK/example.png)

## Video Demonstration

[link](https://youtu.be/CeckZFksqs4)
