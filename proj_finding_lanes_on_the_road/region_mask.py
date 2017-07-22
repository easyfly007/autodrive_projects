import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
import numpy as np 

image = mpimg.imread('test.jpg')
print('the image is ', type(image),
	'with dimentions: ', image.shape)

ysize = image.shape[0]
xsize = image.shape[1]
region_select = np.copy(image)

left_bottom = [0, 539]
right_bottom = [900, 300]
apex = [400, 0]
