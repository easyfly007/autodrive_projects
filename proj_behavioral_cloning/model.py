import keras
import cv2
import numpy as np
import os
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D
from keras.layers import Convolution2D, MaxPooling2D, Activation, Dropout
from keras.layers.convolutional import Conv2D

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

#model.add(Conv2D(24, 5, strides = (2,2), border_mode = 'valid'))
model.add(Convolution2D(24, 5,5,subsample = (2,2), border_mode = 'valid'))
model.add(Activation('relu'))

#model.add(Conv2D(36, 5, strides = (2,2), border_mode = 'valid'))
model.add(Convolution2D(36, 5,5, subsample =  (2,2), border_mode = 'valid'))
model.add(Activation('relu'))

#model.add(Conv2D(48, 5, strides = (2,2), border_mode = 'valid'))
model.add(Convolution2D(48, 5, 5, subsample = (2,2), border_mode = 'valid'))
model.add(Activation('relu'))

#model.add(Conv2D(64, 3, strides = (1,1), border_mode = 'valid'))
model.add(Convolution2D(64, 3,3, subsample = (1,1), border_mode = 'valid'))
model.add(Activation('relu'))

#model.add(Conv2D(64, 3, strides = (1,1), border_mode = 'valid'))
model.add(Convolution2D(64, 3, 3, subsample = (1,1), border_mode = 'valid'))
model.add(Activation('relu'))

model.add(Flatten())

model.add(Dense(100))
model.add(Activation('relu'))

model.add(Dense(50))
model.add(Activation('relu'))

model.add(Dense(10))
model.add(Activation('relu'))

model.add(Dense(1))

model.compile(loss = 'mse', optimizer = 'adam')

# not use a generator
model.fit(X_train, y_train, validation_split = 0.2, shuffle = True, nb_epoch = 5)

# # use a generator
# def train_generator(samples, batch_size):
# 	num_samples = len(samples)
# 	while True: #endless loop, the stop condition is controlled in git_generator parameters
# 		shuffle(samples)
# 		for offset in range(0, num_samples, batch_size):
# 			batch_samples = samples[offset: offset + batch_size]
# 			images = []
# 			labels = []
# 			for batch_sample in batch_samples:
# 				name = './IMG/' + batch_sample[0].split('/')[-1]
#     center_image = cv2.imread(name)
#     center_angle = float(batch_sample[3])
            #     images.append(center_image)
            #     angles.append(center_angle)

            # # trim image to only see section with road
            # X_train = np.array(images)
            # y_train = np.array(angles)
            # yield sklearn.utils.shuffle(X_train, y_train)

# compile and train the model using the generator function
train_generator = generator(train_samples, batch_size=32)
validation_generator = generator(validation_samples, batch_size=32)



# model.fit_generator(train_generator, samples_per_epoch= 
# 	len(train_samples), validation_data=validation_generator, 
# 	nb_val_samples=len(validation_samples), nb_epoch=3)

model.save('model_1.h5')
