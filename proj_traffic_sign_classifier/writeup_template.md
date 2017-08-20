# **Traffic Sign Recognition** 
----
### 0. summary


**Build a Traffic Sign Recognition Project**
in this project, we will build a deep neural network to do traffic sign classification.

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report

**codes**
the rew project material can be found at:
 [project code](https://github.com/udacity/CarND-Traffic-Sign-Classifier-Project/blob/master/Traffic_Sign_Classifier.ipynb)
 my work start from this materials there.

and my project codes can be found at:
 [project code](https://github.com/easyfly007/CarND-Traffic-Sign-Classifier-Project/blob/master/Traffic_Sign_Classifier.ipynb)

----

### 1. Data Set Summary & Exploration

In this project, I use a traffic signs data set from German Traffic Sign Dataset. 

you can download it from below link as I use, [download ](https://d17h27t6h515a5.cloudfront.net/topher/2017/February/5898cd6f_traffic-signs-data/traffic-signs-data.zip) . This is a pickled dataset in which we've already resized the images to 32x32.


I used the python list operation to calculate summary statistics of the traffic signs data set:

* The size of training set is 34799
* The size of the validation set is 4410
* The size of test set is 12630
* The shape of a traffic sign image is [32,32,3]
* The number of unique classes/labels in the data set is 43

----
#### 2.  exploratory visualization of the dataset.
below is a quick peak of the samples, to look at what they look like:
**sample 1**
this is from the # 0 train sample:
![training sample #0](https://github.com/easyfly007/autodrive_projects/blob/master/proj_traffic_sign_classifier/examples/train0.png)
the label is **41 'End of no passing'**


![training sample #233](https://github.com/easyfly007/autodrive_projects/blob/master/proj_traffic_sign_classifier/examples/train233.png)
the label is **31 Wild animals crossing**

![training sample #667](https://github.com/easyfly007/autodrive_projects/blob/master/proj_traffic_sign_classifier/examples/train667.png)
the label is **31 Wild animals crossing**

![training sample #908](https://github.com/easyfly007/autodrive_projects/blob/master/proj_traffic_sign_classifier/examples/train908.png)
the label is **36, Go straight or right **

we can see like the training sample #233 and #667, they show different traffic sign, but one is brighter and one is darker.

### Design and Test a Model Architecture

As a first step, I decided to convert the images to grayscale because the classical LeNet use gray scale, and it will significantly reduce the calculation.

Here is an example of a traffic sign image before and after grayscaling.

![alt text][image2]

As a last step, I normalized the image data because normalization will in some degree avoid gradient vanish problem.


My final model consisted of the following layers:

| Layer         		|     Description	        					| 
|:---------------------:|:---------------------------------------------:| 
| Input         		| 32x32x1 gray scale image   							| 
| Convolution 5x5     	| 1x1 stride, valid padding, outputs 28x28x6 	|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 14x14x6 				    |
| | |
| Convolution 5x5     	| 1x1 stride, valid padding, outputs 10x10x16 	|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 5x5x16 				    |
| | |
| Fully connected		|  outputs 120.        						   |
| Fully connected		|  outputs 84.        						   |
| Fully connected		|  outputs 43.        						   |
| Softmax				|          									|

 


#### 3. Describe how you trained your model. The discussion can include the type of optimizer, the batch size, number of epochs and any hyperparameters such as learning rate.

To train the model, I set super parameters as below:
batch_size: 128
learning_rate: 0.001
and before reloading the data for each epoch, use shuffle to randomize the data.



My final model results were:
* validation set accuracy of  0.658
* test set accuracy of 0.619





### (Optional) Visualizing the Neural Network (See Step 4 of the Ipython notebook for more details)
####1. Discuss the visual output of your trained network's feature maps. What characteristics did the neural network use to make classifications?


