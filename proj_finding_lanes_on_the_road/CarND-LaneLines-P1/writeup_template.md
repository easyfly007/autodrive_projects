# **Finding Lane Lines on the Road** 


---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. 

####  I. converted the images to grayscale
#### 2. to do blur for the raw image to remove some noise pixels
#### 3. during canny function to delect the edge image
#### 4. select the region we care about the lane line
#### 5. do hough line function to get the lane lines, for both left side and right side
#### 6. draw the lane line on the raw image

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by 
#### 1. collect all the lines, separate them into left line and right, based on the slope value (left line slope >0 while right line slope < 0)
#### 2. calculate the avarage slope and bias for both left line and right lines
#### 3. also collect the y axis range, e.g., y_max and y_min, used for both left line and right line
#### 4. write single line with the average slope and average bias for the both left/right lane, end point is at the y_max and y_min

by this way, we got continuous lane lines~~

![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline

when there's corss road ahead, this function may fail and the calcualted left lane/right lane not reasonable.

and if the road is turning left or right, then we may find all line slope positive or negative. then only one side lane will be plotted.


### 3. Suggest possible improvements to your pipeline

a solution for the road turning left or right is that we classify the lines to 2 groups, not only by slope positive or negative,

but by the value near by as a cluster.
