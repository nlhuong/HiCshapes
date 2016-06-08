from __future__ import print_function
import numpy as np
import glob, os, sys
import csv
import random
np.random.seed(1337)  # for reproducibility

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils

batch_size = 64
nb_classes = 6
nb_epoch = 20

# input image dimensions
img_rows, img_cols = 100, 100
# number of convolutional filters to use
nb_filters = 256
# size of pooling area for max pooling
nb_pool = 2
# convolution kernel size
nb_conv = 5

# the data, shuffled and split between train and test sets
#(X_train, y_train), (X_test, y_test) = mnist.load_data()
#print(X_train.shape)

'''x = []
for f in glob.glob(sys.argv[1]+"/*.npy"):
    l = np.load(f)
    if(l.shape[0] != 100):
        continue
    x.append(l)
X_train = np.array(x)
'''
x = []
x_test = []
x_test_name = []
y = []
y_test = []
with open("all-labels.csv") as f:
    reader = csv.reader(f, delimiter=',')
    for line in reader:
        l = np.load("numpy/"+line[0])
        if l.shape[0] != 100:
            print(line[0] + " no good")
        else:
            if np.random.random() < 0.1:
                x_test.append(l)
                y_test.append(int(line[1])-1)
                x_test_name.append(line[0])
            else:
                x.append(l)
                y.append(int(line[1])-1)
X_train = np.array(x)
y_train = np.array(y)
X_test = np.array(x_test)
y_test = np.array(y_test)


X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols)
X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
print('X_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)

model = Sequential()

model.add(Convolution2D(nb_filters, 7, 7,
                        border_mode='valid',
                        input_shape=(1, img_rows, img_cols)))
model.add(Activation('relu'))
model.add(Convolution2D(nb_filters, 5, 5))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adadelta',
              metrics=['accuracy'])

model.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=nb_epoch,
          verbose=1, validation_split=0.1)#validation_data=(X_test, Y_test))
score = model.evaluate(X_test, Y_test, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])


predictions = np.argmax(model.predict(X_test), axis=1)
labels = np.argmax(Y_test, axis=1)
for i in xrange(len(X_test)):
    if predictions[i] != labels[i]:
        print("%s %d %d" % (x_test_name[i], predictions[i], labels[i]))


