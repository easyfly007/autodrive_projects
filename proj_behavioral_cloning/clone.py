import csv
import keras
import cv2
import numpy as np
import os
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D
from keras.layers import Convolution2D, MaxPooling2D, Activation, Dropout

lines = []
with open('./data/driving_log.csv') as csvfile:
	reader = csv.reader(csvfile)
	for line in reader:
		lines.append(line)

images = []
measurements = []
for line in lines:
	# as the image is from windows, use \\ as separator
	measurement = float(line[3])
	measurements.append(measurement)

	# center 
	fullname = line[0]
	filename = fullname.split('\\')[-1]
	current_path = './data/IMG/' + filename
	image = cv2.imread(current_path)
	images.append(image)

	#left camera
	measurements.append(measurement + 0.2)
	fullname = line[1]
	filename = fullname.split('\\')[-1]
	current_path = './data/IMG/' + filename
	image = cv2.imread(current_path)
	images.append(image)

	#right camera
	measurements.append(measurement - 0.2)
	fullname = line[1]
	filename = fullname.split('\\')[-1]
	current_path = './data/IMG/' + filename
	image = cv2.imread(current_path)
	images.append(image)


augmented_images, augmented_measurements = [], []
for image, measurement in zip(images, measurements):
	augmented_images.append(image)
	augmented_measurements.append(measurement)
	augmented_images.append(cv2.flip(image, 1))
	augmented_measurements.append(measurement * (-1.0))

X_train = np.array(augmented_images)
y_train = np.array(augmented_measurements)

model = Sequential()
model.add(Lambda(lambda x:x/255.0 - 0.5, input_shape = (160, 320, 3)))
model.add(Cropping2D(cropping = ((70, 25), (0, 0))))

model.add(Convolution2D(6, 5, 5, border_mode = 'valid'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Activation('relu'))

model.add(Convolution2D(16, 5, 5, border_mode = 'valid'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(84))
model.add(Activation('relu'))

model.add(Dense(1))

model.compile(loss = 'mse', optimizer = 'adam')
model.fit(X_train, y_train, validation_split = 0.2, shuffle = True, nb_epoch = 2)
model.save('model.h5')