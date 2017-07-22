import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
import numpy as np 

image = mpimg.imread('test.jpg')
print('the image is ', type(image),
	'with dimentions: ', image.shape)

# pull out the x and y sizes and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]
region_select = np.copy(image)

#define a triangle region of interest
# keep in mind the origin (x=0, y=0) is in the upper left in image processing
# Note: if you run this code, you'll find these are not sensible values
# but you'll get a chance to play with them soon in q quiz
left_bottom = [0, 539]
right_bottom = [900, 300]
apex = [400, 0]

fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

# find the region inside the lines
xx, yy = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
region_thresholds = (yy > (xx*fit_left[0] + fit_left[1])) & \
	(yy > (xx*fit_right[0] + fit_right[1])) & \
	(yy > (xx*fit_right[0] + fit_right[1])) & \
	(yy < (xx*fit_bottom[0] + fit_bottom[1]))

# coor pixels red which are inside the region of interest
region_select[region_thresholds] = [255, 0, 0]
plt.imshow(region_select)
plt.show()