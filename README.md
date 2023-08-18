# professional project name

Do you like throwing bread at ducks? Well stop it.

TL;DR: Multiple studies (lost the sources lol oops) show that bread is NOT HEALTHY for ducks. So don't throw bread at ducks. If you are hanging out at your local pond or whatever environment happens to have beavers or ducks or fish or frogs or herons or geese or turtles, you can now upload a picture of an animal listed above to see what it eats. Apparently you're not supposed to feed wild animals at all so this is still technically good for information. Even if it's only 7 pieces of information. If I wasn't so incompetent as to try to make my own miserable dataset rather than searching a little better online then I probably could have done a lot more categories. Too bad

image: duck giving a thumb up

## The Algorithm

This project uses a resnet-18 model that is retrained to focus on different types of animals found near ponds: beavers, ducks, fish, frogs, herons, geese, and turtles. The model takes an image and classifies it as one of these seven animals, and then the algorithm creates a copy of the image with text boxes that show the animal name and the diet of that animal.

## Running this project

1. make sure you install things on the jetson nano i don't actually know what this was meant to be let me just check every canvas module ever real quick
2. go to jetson-inference/python/training/classification/data/
3. download data into training/classification/data/
4. go to jetson-inference
5. ./docker/run.sh into jetson-inference/python/training/classification
6. train.py parameter parameter parameter
7. export onnx i forgot what the script was called and my ssh is not working so i can not see
8. type exit to exit the docker i guess
9. go to home/nvidia/pond/ for lack of a better or more logical name
10. python3 pond_imagenet.py {image file path} {file path for output}
11. ignore how the model has like 30% accuracy 

[View a video explanation here UNFORTUNATELY i do not have one currently haha](video link)
