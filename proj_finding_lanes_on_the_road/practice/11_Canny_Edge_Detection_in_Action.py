import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
image = mpimg.imread('exit-ramp.jpg')
plt.imshow(image)
plt.show()

import cv2

image = mpimg.imread('exit-ramp.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

kernel_size = 5
blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

low_threshold = 40
high_threshold = 120
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
plt.imshow(edges, cmap = 'Greys_r')
plt.show()