# **Behavioral Cloning** 
-- by Yifei Huang (easyfly.huang@gmail.com)

---

**Behavioral Cloning Project**

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

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* writeup_report.md or writeup_report.pdf summarizing the results

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

#### 3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

My model consists of a convolution neural network which contains:
** data normalization layer, makes the data range (-1.0, 1.0)
** cropping the images layer, remove the top 70 pixels and bottom 25 pixels
** conv layer, with kernel size 5*5 and kernel count 24
** max pooling layer, with pooling size 2*2
** relu activation layere

** conv layer, with kernel size 5*5 and kernel count 36
** max pooling layer, with pooling size 2*2
** relu activation layer

** conv layer, with kernel size 5*5 and kernel count 48
** max pooling layer, with pooling size 2*2
** relu activation layer

** conv layer, with kernel size 3*3 and kernel count 64
** relu activation layer

** conv layer, with kernel size 3*3 and kernel count 64
** relu activation layer
** dropout layer, with dropout probability = 0.5

** flattern layer
** fully connected layer to 100 output neurons
** relu activation layer
** fully connected layer to 1 output neurons


#### 2. Attempts to reduce overfitting in the model

The model contains dropout layer in order to reduce overfitting (see above detail layers in the model)

To avoid overfitting, we need to collect more and more data, expecially to cover all different driving situlations.
which means, clock wise and anti-clock wise driving, recover from the road side to the center, U-turns.

I try to extract the data collection codes to function loadImages() to make it easily reuse it and load data from different recording source.

the data1 fir and data2 are collected from different drive situations.

also data augment method used, including:
** use the left/center/right camera images.
I manually added the steering value +0.4 for the left camera images label, the  lectures suggest + 0.2, but in my test, +0.4 seems to be bettere.
** crop the top 70 pixels and bottom 25 pixels, which will reduce the input data size, and reduce the complexity of the model
** flip the left/right of the images, which will enlarge the dataset *2


#### 3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually

#### 4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I used a combination of center lane driving, recovering from the left and right sides of the road.

For details about how I created the training data, see the next section. 

### Model Architecture and Training Strategy

#### 1. Solution Design Approach

The overall strategy for deriving a model architecture was evaluation by the advices on the lecture video.

My first step was to use a convolution neural network model similar to the LeNet.
I thought this model might be appropriate because LeNet is always considered as the first thought in the mind as it's the first convolutional network in the history.

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set. I found that my first model had a low mean squared error on the training set but a high mean squared error on the validation set. This implied that the model was overfitting. 

To combat the overfitting, I try to collect more datas.

Then I retrained the models again with the new dataset. 
Then I observed that 

The final step was to run the simulator to see how well the car was driving around track one. There were a few spots where the vehicle fell off the track... to improve the driving behavior in these cases, I ....

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

#### 2. Final Model Architecture

The final model architecture (model.py lines 18-24) consisted of a convolution neural network with the following layers and layer sizes ...

Here is a visualization of the architecture (note: visualizing the architecture is optional according to the project rubric)

![alt text][image1]

####3. Creation of the Training Set & Training Process

To capture good driving behavior, I first recorded two laps on track one using center lane driving. Here is an example image of center lane driving:

![alt text][image2]

I then recorded the vehicle recovering from the left side and right sides of the road back to center so that the vehicle would learn to .... These images show what a recovery looks like starting from ... :

![alt text][image3]
![alt text][image4]
![alt text][image5]

Then I repeated this process on track two in order to get more data points.

To augment the data sat, I also flipped images and angles thinking that this would ... For example, here is an image that has then been flipped:

![alt text][image6]
![alt text][image7]

Etc ....

After the collection process, I had X number of data points. I then preprocessed this data by ...


I finally randomly shuffled the data set and put Y% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. The ideal number of epochs was Z as evidenced by ... I used an adam optimizer so that manually training the learning rate wasn't necessary.
