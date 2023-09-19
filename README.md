# Clothes Recognition Using CNN model
## What is CNN Model
A convolutional neural network (CNN) is a type of deep learning algorithm that is particularly well-suited for image recognition and processing tasks. CNNs are inspired by the structure of the human visual cortex, which is made up of layers of neurons that are specialized for detecting different types of features in images.

CNNs typically consist of two main types of layers: convolutional layers and pooling layers. Convolutional layers learn to detect specific features in the input image, such as edges, corners, and shapes. Pooling layers reduce the size of the output from the convolutional layers, while still preserving the most important information.

CNNs are able to learn complex features from images by stacking multiple convolutional and pooling layers together. Each layer learns to detect more complex features than the previous layer. For example, the first layer might learn to detect edges and corners, while the second layer might learn to detect shapes like eyes, noses, and mouths. The last layer of the CNN typically outputs a probability distribution over the different classes of objects that could be present in the image.

## Steps to create model that can predict the type of clothes
### Step 1 - Collect images of diffrent clothing
We click pitures of clothes and also use piture from internet then divide the images into different classes and uplode it in Google Drive in diffrent folder that are train, test and validation 
train folder has 70% images test has 20% and validation has 10% data

### Step 2 - Build the model and test the accuracy
1 We use Python tensorflow library to develop a model 

2 we use Sequential model to train model

3 we added three convolution layer and 3 hidden layers in our model

4 after that we do hyperparameter tuning

5 then train the data and find it accuracy

6 then we use test data to test the final accuray of model and use accuracy and val accuracy to plot a graph

### Step 3 - Create a interface 
now we use gradio to create interface where we can uplode the clothes image and our model can predict it
