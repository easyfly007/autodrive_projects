# **Behavioral Cloning** 
-- by Yifei Huang (easyfly.huang@gmail.com)

---

## Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./examples/placeholder.png "Model Visualization"
[image2]: ./examples/placeholder.png "Grayscaling"
[image3]: ./examples/placeholder_small.png "Recovery Image"
[image4]: ./examples/placeholder_small.png "Recovery Image"
[image5]: ./examples/placeholder_small.png "Recovery Image"
[image6]: ./examples/placeholder_small.png "Normal Image"
[image7]: ./examples/placeholder_small.png "Flipped Image"

----

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
    * here my file is model_7.h5, as in the project period, I tested different version of models and then model_7.h5 is the final version.
    * anyway, you can rename it back to model.h5, I think the name is not an import issue.
* writeup_report.md or writeup_report.pdf summarizing the results

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model_7.h5
```

#### 3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

----

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

My model consists of a convolution neural network, which is copyied from Nvidia's report 
https://devblogs.nvidia.com/parallelforall/deep-learning-self-driving-cars/
which contains:
* data normalization layer, makes the data range (-1.0, 1.0)
    * actually in my model it's range (-0.5, 0.5), I think both (-1.0, 1.0) and (-0.5, 0.5) are OK.   
* cropping the images layer, remove the top 70 pixels and bottom 25 pixels
* flip left/right the images, and the label value will multipy -1.0 accordingly
    * this will enlarge the data size and also fit for left turn and right turn conditions   
* conv layer 1, with kernel size 5*5 and kernel count 24, kernel stride 2*2
    * no following max pooling layer, as I used a 2*2 stride
* relu activation layere
* conv layer 2, with kernel size 5*5 and kernel count 36, kernel stride 2*2
    * no following max pooling layer, as I used a 2*2 stride
* relu activation layere
* conv layer 3, with kernel size 5*5 and kernel count 48, kernel stride 2*2
    * no following max pooling layer, as I used a 2*2 stride
* relu activation layere
* conv layer 4, with kernel size 3*3 and kernel count 64, kernel stride 1*1
    * no following max pooling layer
* relu activation layere
* conv layer 5, with kernel size 3*3 and kernel count 64, kernel stride 1*1
    * no following max pooling layer
* relu activation layere
* flattern layer
* fully connected layer to 100 output neurons
* relu activation layer
* fully connected layer to 50 output neurons
* relu activation layer
* fully connected layer to 10 output neurons
* relu activation layer
* fully connected layer to 1 output neurons


#### 2. Attempts to reduce overfitting in the model

to avoid overfitting, I tried many different methods.
* add more datas
    * I used all the 3 cameras's image as the input, the left, the centern and the right one
    * +0.2 for the left image label, -0.2 for the right imagelabel
    * left/right shift the images, like we are both running clock-wise and anti-clockwise trip.
    * crop the top and bottom of the image, this will reduce the models complexity and the parameters number to learn.
    * add some special condition that will not covered by a normal run
        * like how a car recovder from the side to the center
    * add more images samples we should pay special attention
        * how to take a large angle left/right turn
        * in condition there's no lane line
        
from the model.py, you can see some I load data from different files, which contain different training data
also I try to extract the data collection codes to function loadImages() to make it easily reuse it and load data from different recording source.

* epoch selection
    * in my testing, the first model, I use the udacity provided dataset as the training set, run epoch 5, then I see loss as below:
        * epoch 1: train loss = 0.0375, valid loss = 0.0378
        * epoch 2: train loss = 0.0364, valid loss = 0.0373
        * epoch 3: train loss = 0.0362, valid loss = 0.0367
        * epoch 4: train loss = 0.0360, valid loss = 0.0368
        * epoch 5: train loss = 0.0359, valid loss = 0.0369

you can see as we have more train epochs, train loss continus decrease, but valid loss increased after epoch3, seems after 3 epoch training, the model is try to learn the unique feature in the training dataset, not the general features. So I selected epoch = 3 for all the following model training.
    


#### 3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually

#### 4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I used a combination of center lane driving, recovering from the left and right sides of the road.

For details about how I created the training data, see the next section. 

------

### Model Architecture and Training Strategy

#### 1. Solution Design Approach

The overall strategy for deriving a model architecture was evaluation by the advices on the lecture video.

My first step was to build a linear regression to make sure the flow can work.
of course in autonomous mode, the car runs terribley, but it can be improved.


My second step was to use a convolution neural network model similar to the LeNet.

I thought this model might be appropriate because LeNet is always considered as the first thought in the mind as it's the first convolutional network in the history.

I try to generate some normal user drive data by my self for training, but actually it's difficult to generate high quality data than udacity provided.
so I use udacity provided data as the training data for the normal run condition.

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set (0.8 for train, 0.2 for validation). I found that my first model had a comparable mean squared error on the training and validation set. but the result on the autonomous mode is not very well. this means mybe I need a more powerful model

then I read the Nvidia paper and borrowed idea from there, you can see my final model in above session.
this model is more complicated than LeNet, and more parameters to be learned.

To combat the overfitting, I try to do some data augmentation. see above sessions.

Then I retrained the models again with the new dataset. 

Then I observed that in most of the condition, the car runs perfectly well, but in some large angle left turn, it failed.
which means it's not enough trained on such condition, and also not enough trained on how to recover from the side of the road.

then I added more specific data to fix this. see above session.

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

#### 2. Final Model Architecture

The final model architecture (model.py lines 29-64) consisted of a convolution neural network (see above sessions)

Here is a visualization of the architecture (note: visualizing the architecture is optional according to the project rubric)
![final model][image2]: ./nvidianet.png "final net structures "


#### 3. Creation of the Training Set & Training Process

in my training step, I firstly try to train on my PC laptop, but it's too slow.
then I switched to a linux server with 2 tesla T100 GPU, which is much more faster.

To capture good driving behavior, I used udacity provided dataset as the normal run condition.

I then recorded the vehicle recovering from the left side and right sides of the road back to center so that the vehicle would learn to revoce back to the reoad in some case it fell off the road.

To augment the data sat, I also flipped images and angles thinking that this would ... For example, here is an image that has then been flipped:

After the collection process, I had 59520 number of data points.

I finally randomly shuffled the data set and put 20% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. The ideal number of epochs was 3, as I explained in the above session.

I used an adam optimizer so that manually training the learning rate wasn't necessary.

