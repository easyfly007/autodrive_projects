## Writeup report for vehicle detection project


---

### Vehicle Detection Project

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector. 
* normalize features and randomize a selection for training and testing.
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run a pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

[//]: # (Image References)
[image1]: ./examples/car_not_car.png
[image2]: ./examples/HOG_example.jpg
[image3]: ./examples/sliding_windows.jpg
[image4]: ./examples/sliding_window.jpg
[image5]: ./examples/bboxes_and_heat.png
[image6]: ./examples/labels_map.png
[image7]: ./examples/output_bboxes.png
[video1]: ./project_video.mp4

need to meet all the [Rubric](https://review.udacity.com/#!/rubrics/513/view) Points to complete the project.

---

### Writeup / README

* this writeup report is based on the template provided by udacity in [Here](https://github.com/udacity/CarND-Vehicle-Detection/blob/master/writeup_template.md).


### Histogram of Oriented Gradients (HOG)
* 
The code for this step is contained in the code cell 9 by the function get_hog_features() of the IPython notebook solution.ipynb.

I started by reading in all the `vehicle` and `non-vehicle` images.  Here are 2  example of `vehicle` and `non-vehicle` images:

![car img](examples/car_templates/3.jpeg)
car image

![not car img](examples/notcar_templates/extra34_144.jpeg)
not car image

* I then explored different color spaces and different `skimage.hog()` parameters (`orientations`, `pixels_per_cell`, and `cells_per_block`).  I grabbed random images from each of the two classes and displayed them to get a feel for what the `skimage.hog()` output looks like.

Here is an example using the `Gray` color space and HOG parameters of `orientations = 9`, `pixels_per_cell = (8, 8)` and `cells_per_block = (2, 2)`:


![car hog image](examples/car_hog.png)


#### 2. final choice of HOG parameters.

* I tried various combinations of parameters, like the RGB, YCrCb, Gray

finally I selected YCrCb and combine all the 3 channel together.
the parameter I used for hog is:

`orient = 9, pix_per_cell = 8, cell_per_block = 2 `

and I use all the 3 channels and then concatenate them together as the features.


#### 3. train a classifier using the selected features

* in this project, SVM is used as the classifier.

there's some parameters to tune, like the C and kernel type.
I selecte the linear kernel, and tunned C = 0.02, loss = hinge
by a grid search.


* for the dataset build, I selected all the vehicle and non-vehicle png images.

I use the color spatial + histogram + HOG as the sample features.

* then I do normalizes them to make sure all the features (from hog, color space spatial, color histogram) has the same scale.

* then I shuffle the dataset, make the car and not car samples randomly distributed.

* after that, I split the dataset, 80% for traning, 20% for testing.
the tested accuracy is 98.7% which seems quite good.

* the classifier and scaler will be used for the video image processing,
so I use pickle to save them to avoid retrain when I continue the project next time.


### Sliding Window Search

##### 1.  implemented a sliding window search.

* the training image is small size and has only car (if label as positive)
so I did a sliding window method to check if the car detected in each window.

the basic windows size  is (64, 64), and it can be scalled as 1.0, 1.5, 2.0 to detect larger cars.

smaller window sliding range is from the road end to bottom, while the larger window is alitter lower.
it's reasonable that the nearer car will appear larger in the img.

I use the y range for each scale is:
scale = 1.0, y range = [350, 520]
scale = 1.5, y range = [400, 600]
scale = 2.0, y range = [450, 650]

##### 2. pipe line for image vehicle detection


Ultimately I searched cars using YCrCb 3-channel HOG features plus spatially binned color and histograms of color in the feature vector, which provided a nice result.

the total feature is 8460, including spatial features (32*32*3 = 3072), color space histogram features (32*3 = 96), HOG features for 3 channel (5292).


then I applied multi scaled windows sliding search of cars in the  input image.
the scaling factor and y range similar with above.

use the normalizer (scaler) previously fitted to do transformation to make sure all the features are in the same value scale.

I calculated heat map for the car detection, using threshold = 4 to select the space that I use to make car bbox.

label function from scipy.ndimage.measurements is used to make the range of the cat detection.

then this raw image with the final rectangle are saved in the output_images folder, with the same file name.
also some intermedian image saved in the same folder, with a self-explainable pre or post suffix.


---

### Video Implementation

##### 1. final video output
the final test video result is test_solution1.mp4, test_soltuin2.mp4, and test_solution3.mp4, which used different method (expained below).

the final project video result is proj_solution2.mp4 and proj_solution3.mp4, which I used the third method to do vidoe frame image processing.

* the first method I used is in function video_processing1(), it's the same as img_processing(), process each frame iamge independently.
we can see a lot of false positive detective result

##### 2. filter for false positives and some method for combining overlapping bounding boxes.

* I used the same function like img_processing() to get the vehicle detection in the video, just treat the images for each frame individually.

we can see the result is not very good. a lot of false positive observed (which marked as a car but actually not a car)
the result is in file test_solution1.mp4, and some intermedian images are saved in folder videoimg_test1, which I used to see what happened internally.

* I then try to consider the continuous frame together.

for the second method, I used an accumulated_heat_map to keep the previous frame detected card, and add the new frame heat map to do a final decision.

* the accumulated_heat_map will be decayed with a factor of 0.8 for each frame, so the far away old frame image result will has lower affection.

by this result it's better than the first result
you can compare test_slution1.mp4 and test_solution2.mp4 and find the result.

* the above method is implemented in function video_processing2()

* the third way of continuous frame image handling methodd implemented in video_processing3 function which is:

use the previous 5 frame video image detection, and consider at least 4 frame marked as true pixels.
we mark a car only in condition that the current frame is marked as true and the last 4 in 5 marked as true.

the result is show in test_solution3.mp4


---

### Discussion

*  for speed up, I use the pickle to dump necessary information like the classifier and scaler that I will used next time.

* also for speed up, as recommended by in the course, I firstly calculated the hog matrix then apply the windows sliding.
this can save times when the windows has overlap.

*  the difficult part is hwo to select the efeatures, it will decide your project fail or succeed.
I learned from the class suggestion and used YCrCb as the color space and it seems OK.

* my concern: as we can see the feature length will be as large as 8460, but we only have 8968 not car samples and 8792 car samples.
 will it be over fitting? I am not quite sure, but the test accuracy is good, so I guess that the features are actually not so much,
I mean the features are related, not independent each other.

* for debugging in the video image process functions, I try to save the middle image in a folder that I can check how this pipe like works.
it's great helpful for my work.
