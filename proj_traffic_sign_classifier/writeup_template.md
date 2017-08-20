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


this is from the #233 train sample

![training sample #233](https://github.com/easyfly007/autodrive_projects/blob/master/proj_traffic_sign_classifier/examples/train233.png)

the label is **31 Wild animals crossing**


this is from the #667 train sample

![training sample #667](https://github.com/easyfly007/autodrive_projects/blob/master/proj_traffic_sign_classifier/examples/train667.png)

the label is **31 Wild animals crossing**


this is from the #908 train sample

![training sample #908](https://github.com/easyfly007/autodrive_projects/blob/master/proj_traffic_sign_classifier/examples/train908.png)

the label is **36, Go staight or right**


we can see like the training sample #233 and #667, they show the same traffic sign, but one is brighter and one is darker.


----

### 3. data pre-processing

there are something to do before we build our network and load the data into our network.


**transfer from RGB color image to gray scale image**

generally I will copy the LeNet structure and it use gray scale image as input

just by simply use the mean of the RGB 
    

**input normalization**

divid the inputt by 255, then the scale will be 0.0-> 1.0 

Here is an example of a traffic sign image before and after grayscaling.


![training sample #234, RGB](https://github.com/easyfly007/autodrive_projects/blob/master/proj_traffic_sign_classifier/examples/train234.png)

RGB image for training sample #234
    

![training sample #234, gray](https://github.com/easyfly007/autodrive_projects/blob/master/proj_traffic_sign_classifier/examples/train234_gray.png)

gray image for training sample #234


**data augment (TODO)**

actually I didn't do any augment to expand the dataset.but a reasonable augment technique would be:

1. rotate the image for a small angle (<5 degree)
2. add random noise
3. cut the edge like this techniques

----

### 4. nentwork

My final model consisted of the following layers:


| Layer                 |     Description                               | 
|:---------------------:|:---------------------------------------------:| 
| Input                 | 32x32x1 gray scale image                              | 
| Convolution 5x5       | 1x1 stride, valid padding, outputs 28x28x6    |
| RELU                  |                                               |
| Max pooling           | 2x2 stride,  outputs 14x14x6                  |
| Convolution 5x5       | 1x1 stride, valid padding, outputs 10x10x16   |
| RELU                  |                                               |
| Max pooling           | 2x2 stride,  outputs 5x5x16                   |
| Fully connected       |  outputs 120.                                |
| drop out      |  0.75 keep_prob for training, 1.0 for evaluation     |
| Fully connected       |  outputs 120.                                |
| drop out      |  0.75 keep_prob for training, 1.0 for evaluation     |
| Fully connected       |  outputs 43.                                 |
| Softmax               |                                           |


this structure is copied from the classic LeNet structure (while I added drop out in the last 2 FC layers), for more detail, see below link:
http://yann.lecun.com/exdb/lenet/


**computer graph illustration**
by using tensorboard, the computer graph is as below:

![ent graph](https://github.com/easyfly007/autodrive_projects/blob/master/proj_traffic_sign_classifier/examples/computer_graph1.png)


#### 5. hyper parameters setting

the hyper parameters we selected:

**epoch**

even though the larger epoch we select, the higher accuracy (lower loss value) we will got in the training set. but in my testing, a large will induce over fitting, e.g., the accuracy becomes lower in the validation set as we train more and more.

it's because in the large epoch iterations, it's learning the the pecific features from the training set, not the general features. so need to do an early stop here.

in my testing, I select near 15 epochs and stops it there.


**learning rate**

learning rate is not a big problem, if you are not sure which one to use, start from the stardard 0.001, and a samll one will always induce a better result except need larger epoch numbersd.

in my case, I select 0.001.


**batch size**

it's based on your machine memory size.

if accept, select a larger one.

I selet 128.

it's OK in my PC, the only problem is that when in the fine tuning step, after several try, the memory depleted and I will need to restart the kernel to clean on the memory.

do a random shuffle before each epoch.


**optimizer**

I select the AdamOptimizer, rather than GradientDescentOptimizer,
as for GradientDescentOptimizere, it may stuck on the local minimum point there.


### 5. the final solution 

My final model results were:

* training set accuracy of 0.893
* validation set accuracy of 0.872
* test set accuracy of 0.863



### 6. Visualizing the Neural Network

(See Step 4 of the Ipython notebook for more details)

####1. Discuss the visual output of your trained network's feature maps. What characteristics did the neural network use to make classifications?


