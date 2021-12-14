# -*- coding: utf-8 -*-
"""Road_Surface_New.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16Nt78tKBkI-UA5OGFeK-LYsHRHiCY-8m
"""

from google.colab import drive
drive.mount('/content/drive')

from google.colab import files
files.upload()

import dataset
import keras
import tensorflow as tf
import time
from datetime import timedelta
import math
import random
import numpy as np
import os

#Adding Seed so that random initialization is consistent
from numpy.random import seed
seed(1)
tf.random.set_seed(2)

import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
train=ImageDataGenerator(rescale=1/255)
validation=ImageDataGenerator(rescale=1/255)
train_dataset=train.flow_from_directory('/content/drive/MyDrive/Dataset/Training_Road surface',
                                        target_size=(200,200), batch_size=3, class_mode='binary')

validaition_dataset=train.flow_from_directory('/content/drive/MyDrive/Dataset/Validation_Road Surface',
                                        target_size=(200,200), batch_size=3, class_mode='binary')

train_dataset.class_indices

model=tf.keras.models.Sequential([tf.keras.layers.Conv2D(16,(3,3), activation = 'relu', input_shape=(200,200,3)),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      #
                                      tf.keras.layers.Conv2D(16,(3,3), activation='relu'),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      #
                                      tf.keras.layers.Conv2D(16,(3,3), activation='relu'),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      ##
                                      tf.keras.layers.Flatten(),
                                      ##
                                      tf.keras.layers.Dense(512, activation='relu'),
                                      ##
                                      tf.keras.layers.Dense(1, activation='sigmoid')])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit=model.fit(train_dataset, steps_per_epoch=3, epochs=2000, validation_data= validaition_dataset)

train_Asphalt=ImageDataGenerator(rescale=1/255)
validation_Asphalt=ImageDataGenerator(rescale=1/255)
train_dataset_Asphalt=train.flow_from_directory('/content/drive/MyDrive/Dataset/Training/Asphalt',
                                        target_size=(200,200), batch_size=3, class_mode='binary')

validaition_dataset_Asphalt=train.flow_from_directory('/content/drive/MyDrive/Dataset/Training/Asphalt',
                                        target_size=(200,200), batch_size=3, class_mode='binary')

train_dataset_Asphalt.class_indices

model_Asphalt=tf.keras.models.Sequential([tf.keras.layers.Conv2D(16,(3,3), activation = 'relu', input_shape=(200,200,3)),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      #
                                      tf.keras.layers.Conv2D(16,(3,3), activation='relu'),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      #
                                      tf.keras.layers.Conv2D(16,(3,3), activation='relu'),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      ##
                                      tf.keras.layers.Flatten(),
                                      ##
                                      tf.keras.layers.Dense(512, activation='relu'),
                                      ##
                                      tf.keras.layers.Dense(1, activation='sigmoid')])

model_Asphalt.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model_Asphalt.fit=model_Asphalt.fit(train_dataset_Asphalt, steps_per_epoch=3, epochs=2000, validation_data= validaition_dataset)

train_MudClay=ImageDataGenerator(rescale=1/255)
validation_MudClay=ImageDataGenerator(rescale=1/255)
train_dataset_MudClay=train.flow_from_directory('/content/drive/MyDrive/Dataset/Training/Mud & Clay',
                                        target_size=(200,200), batch_size=3, class_mode='binary')

validaition_dataset_MudClay=train.flow_from_directory('/content/drive/MyDrive/Dataset/Training/Mud & Clay',
                                        target_size=(200,200), batch_size=3, class_mode='binary')

train_dataset_MudClay.class_indices

model_MudClay=tf.keras.models.Sequential([tf.keras.layers.Conv2D(16,(3,3), activation = 'relu', input_shape=(200,200,3)),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      #
                                      tf.keras.layers.Conv2D(16,(3,3), activation='relu'),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      #
                                      tf.keras.layers.Conv2D(16,(3,3), activation='relu'),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      ##
                                      tf.keras.layers.Flatten(),
                                      ##
                                      tf.keras.layers.Dense(512, activation='relu'),
                                      ##
                                      tf.keras.layers.Dense(1, activation='sigmoid')])

model_MudClay.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model_MudClay.fit=model_MudClay.fit(train_dataset_MudClay, steps_per_epoch=3, epochs=2000, validation_data= validaition_dataset)

train_Paved=ImageDataGenerator(rescale=1/255)
validation_Paved=ImageDataGenerator(rescale=1/255)
train_dataset_Paved=train.flow_from_directory('/content/drive/MyDrive/Dataset/Training/Paved',
                                        target_size=(200,200), batch_size=3, class_mode='binary')

validaition_dataset_Paved=train.flow_from_directory('/content/drive/MyDrive/Dataset/Training/Paved',
                                        target_size=(200,200), batch_size=3, class_mode='binary')

train_dataset_Paved.class_indices

model_Paved=tf.keras.models.Sequential([tf.keras.layers.Conv2D(16,(3,3), activation = 'relu', input_shape=(200,200,3)),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      #
                                      tf.keras.layers.Conv2D(16,(3,3), activation='relu'),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      #
                                      tf.keras.layers.Conv2D(16,(3,3), activation='relu'),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      ##
                                      tf.keras.layers.Flatten(),
                                      ##
                                      tf.keras.layers.Dense(512, activation='relu'),
                                      ##
                                      tf.keras.layers.Dense(1, activation='sigmoid')])

model_Paved.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model_Paved.fit=model_Paved.fit(train_dataset_MudClay, steps_per_epoch=3, epochs=2000, validation_data= validaition_dataset)

train_Rocky=ImageDataGenerator(rescale=1/255)
validation_Rocky=ImageDataGenerator(rescale=1/255)
train_dataset_Rocky=train.flow_from_directory('/content/drive/MyDrive/Dataset/Training/Rocky',
                                        target_size=(200,200), batch_size=3, class_mode='binary')

validaition_dataset_Rocky=train.flow_from_directory('/content/drive/MyDrive/Dataset/Training/Rocky',
                                        target_size=(200,200), batch_size=3, class_mode='binary')

train_dataset_Rocky.class_indices

model_Rocky=tf.keras.models.Sequential([tf.keras.layers.Conv2D(16,(3,3), activation = 'relu', input_shape=(200,200,3)),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      #
                                      tf.keras.layers.Conv2D(16,(3,3), activation='relu'),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      #
                                      tf.keras.layers.Conv2D(16,(3,3), activation='relu'),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      ##
                                      tf.keras.layers.Flatten(),
                                      ##
                                      tf.keras.layers.Dense(512, activation='relu'),
                                      ##
                                      tf.keras.layers.Dense(1, activation='sigmoid')])

model_Rocky.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model_Rocky.fit=model_Rocky.fit(train_dataset_MudClay, steps_per_epoch=3, epochs=2000, validation_data= validaition_dataset)

train_Sandy=ImageDataGenerator(rescale=1/255)
validation_Sandy=ImageDataGenerator(rescale=1/255)
train_dataset_Sandy=train.flow_from_directory('/content/drive/MyDrive/Dataset/Training/Sandy',
                                        target_size=(200,200), batch_size=3, class_mode='binary')

validaition_dataset_Sandy=train.flow_from_directory('/content/drive/MyDrive/Dataset/Training/Sandy',
                                        target_size=(200,200), batch_size=3, class_mode='binary')

train_dataset_Sandy.class_indices

model_Sandy=tf.keras.models.Sequential([tf.keras.layers.Conv2D(16,(3,3), activation = 'relu', input_shape=(200,200,3)),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      #
                                      tf.keras.layers.Conv2D(16,(3,3), activation='relu'),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      #
                                      tf.keras.layers.Conv2D(16,(3,3), activation='relu'),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      ##
                                      tf.keras.layers.Flatten(),
                                      ##
                                      tf.keras.layers.Dense(512, activation='relu'),
                                      ##
                                      tf.keras.layers.Dense(1, activation='sigmoid')])

model_Sandy.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model_Sandy.fit=model_Sandy.fit(train_dataset_MudClay, steps_per_epoch=3, epochs=2000, validation_data= validaition_dataset)

train_Unpaved=ImageDataGenerator(rescale=1/255)
validation_Unpaved=ImageDataGenerator(rescale=1/255)
train_dataset_Unpaved=train.flow_from_directory('/content/drive/MyDrive/Dataset/Training/Unpaved',
                                        target_size=(200,200), batch_size=3, class_mode='binary')

validaition_dataset_Unpaved=train.flow_from_directory('/content/drive/MyDrive/Dataset/Training/Unpaved',
                                        target_size=(200,200), batch_size=3, class_mode='binary')

train_dataset_Unpaved.class_indices

model_Unpaved=tf.keras.models.Sequential([tf.keras.layers.Conv2D(16,(3,3), activation = 'relu', input_shape=(200,200,3)),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      #
                                      tf.keras.layers.Conv2D(16,(3,3), activation='relu'),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      #
                                      tf.keras.layers.Conv2D(16,(3,3), activation='relu'),
                                      tf.keras.layers.MaxPool2D(2,2),
                                      ##
                                      tf.keras.layers.Flatten(),
                                      ##
                                      tf.keras.layers.Dense(512, activation='relu'),
                                      ##
                                      tf.keras.layers.Dense(1, activation='sigmoid')])

model_Unpaved.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model_Unpaved.fit=model_Unpaved.fit(train_dataset_MudClay, steps_per_epoch=3, epochs=2000, validation_data= validaition_dataset)

import cv2 as cv
import numpy as np
import tensorflow as tf
import argparse
import sys
import os.path
import random
import os
import glob
import operator
import time
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
from PIL import Image
from numpy import array

#labelq=''

dir_path='/content/drive/MyDrive/Dataset/Test/Asphalt/Bad'
  
for i in os.listdir(dir_path ):
    img=image.load_img(dir_path+'/'+i, grayscale=False, color_mode='rgb', target_size=(200,200), interpolation='nearest' )
    plt.imshow(img)
    plt.show()

    width = round(img.width)
    height = round(img.height)

    newHeight = int(round(height/2))
    X=image.img_to_array(img)
    X=np.expand_dims(X,axis=0)
    images=np.vstack([X])
    index=model.predict(images)
    if index==1:
      label= 'Asphalt'
      quality=model_Asphalt.predict(images)
      if quality==1:
        labelq='Bad'
      elif quality==2:
        labelq='Good'
      elif quaity==3:
        labelq='Regular'
    if index==2:
      label= 'MudClay'
      quality=model_MudClay.predict(images)
      if quality==1:
        labelq='Bad'
      elif quality==2:
        labelq='Good'
      elif quality==3:
        labelq='Regular'
    if index==3:
      label= 'Paved'
      quality=model_Paved.predict(images)
      if quality==1:
        labelq='Bad'
      elif quality==2:
        labelq='Good'
      elif quality==3:
        labelq='Regular'
    if index==4:
      label= 'Rocky'
      quality=model_Rocky.predict(images)
      if quality==1:
        labelq='Bad'
      elif quality==2:
        labelq='Regular'
    if index==5:
      label= 'Sandy'
      quality=model_Sandy.predict(images)
      if quality==1:
        labelq='Bad'
      elif quality==2:
        labelq='Good'
      elif quality==3:
        labelq='Regular'
    if index==6:
      label= 'Unpaved'
      quality=model_Unpaved.predict(images)
      if quality==1:
        labelq='Bad'
      elif quality==2:
        labelq='Regular'
    print("Type", label)
    print("Quality", labelq)