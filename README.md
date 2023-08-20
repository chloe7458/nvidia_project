# professional project name

Do you like throwing bread at ducks? Well stop it.

TL;DR: Multiple studies (lost the sources lol oops) show that bread is NOT HEALTHY for ducks. So don't throw bread at ducks. If you are hanging out at your local pond or whatever environment happens to have beavers or ducks or fish or frogs or herons or geese or turtles, you can now upload a picture of an animal listed above to see what it eats. Apparently you're not supposed to feed wild animals at all so this is still technically good for information. Even if it's only 7 pieces of information. If I wasn't so incompetent as to try to make my own miserable dataset rather than searching a little better online then I probably could have done a lot more categories. Too bad

image: duck giving a thumb up

### The Algorithm
This project uses a resnet-18 network that is retrained to focus on different types of animals found near ponds: beavers, ducks, fish, frogs, herons, geese, and turtles. The model takes an image and classifies it as one of these seven animals, and then the algorithm creates a copy of the image with labels that show the animal's name and what the animal eats.

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
      <summary>Instructions</summary>
      
      1. Open VSCode and navigate to the Extensions tab.
      
      2. Install the Remote-SSH extension.
      
      3. Navigate to the Command Palette. (View > Command Palette or Ctrl + Shift + P)
      
      4. Select "Remote-SSH: Connect to Host..."
      
      5. Select "Add New SSH Host..."
      
      6. Type "nvidia@" followed by your jetson nano's IP address.
      
      7. Select the first option.
      
      8. Connect to your jetson nano. If asked, select Linux as the platform for the remote host.
      
      9. Enter the password.
      
      10. Select "Open Folder..." and enter "/home/".
   
   </details>

3. Download the data folder to your computer and move the contents into **/home/nvidia/jetson-inference/python/training/classification/data/**.

4. Download the models folder to your computer and move the contents into **/home/nvidia/jetson-inference/python/training/classification/models/pond/**.

5. Open the terminal and navigate to **/home/nvidia/jetson-inference/**.

   ```
   $ cd nvidia/jetson-inference/
   ```
   
7. Open the docker container and enter the password.

   ```
   $ ./docker/run.sh
   ```

8. Navigate to **/jetson-inference/python/training/classification/** in the docker container.

   ```
   # cd python/training/classification/
   ```

9. Re-train the network using the data for this project.

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
         
         Try running the file again and it should work.
         
   </details>

11. Export the re-trained model using this command.

    ```
    # python3 onnx_export.py --model-dir=models/pond
    ```

    You should see the ONNX file in the explorer.
  
12. When you are satisfied with the training, pause again and exit the docker container.

    ```
    # exit
    ```
    
13. You should be back at **/home/nvidia/jetson-inference/**. Navigate to **/home/nvidia/pond/**.

    ```
    $ cd ..
    $ cd pond/
    ```
    
14. To use the model, run ```pond_imagenet.py```.
    This command will make the model process all of the beaver images in the dataset for this project and saves the outputs to **/home/nvidia/pond/output/**.

    ```
    $ python3 pond_imagenet.py ../jetson-inference/python/training/classification/data/pond/test/beaver/"*.jpg" output/"output_%i.jpg"
    ```

    To process your own images, upload them to VSCode and change the file paths in the command.

    also ignore how the model has like 30% accuracy

17. Open the output files in VSCode to see the results.
    
[View a video explanation here UNFORTUNATELY i do not have one currently haha](video link)
