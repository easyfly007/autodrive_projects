import keras
import cv2
import numpy as np
import os
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D
from keras.layers import Convolution2D, MaxPooling2D, Activation, Dropout
from load_data import loadImages

images1, measurements1 = loadImages('./data')
# images2, measurements2 = loadImages('./data2')

# images, measurements = images1 + images2, measurements1 + measurements2
images, measurements = images1, measurements1
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

model.add(Convolution2D(24, 5, 5, border_mode = 'valid'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Activation('relu'))

model.add(Convolution2D(36, 5, 5, border_mode = 'valid'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Activation('relu'))

model.add(Convolution2D(48, 5, 5, border_mode = 'valid'))
# model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Activation('relu'))

model.add(Convolution2D(64, 3, 3, border_mode = 'valid'))
# model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Activation('relu'))


model.add(Convolution2D(64, 3, 3, border_mode = 'valid'))
# model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Flatten())

model.add(Dense(100))
model.add(Activation('relu'))

model.add(Dense(1))

model.compile(loss = 'mse', optimizer = 'adam')
model.fit(X_train, y_train, validation_split = 0.2, shuffle = True, nb_epoch = 5)
model.save('model_3.h5')