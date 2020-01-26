from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten , Dense
from keras import backend as K
import numpy as np 
from keras.preprocessing import image
from keras.models import model_from_json

img_width , img_height = 100,100

X = "C:/Users/hp/PlantVillage/train"
Y = "C:/Users/hp/PlantVillage/test"
X_samples = 400
Y_samples = 100
epochs = 20
batch_size = 25

if K.image_data_format() == "channels_first":
    input_shape = (3, img_width, img_height)
    
else:
    input_shape = (img_width, img_height , 3)
    
    
X_datagen = ImageDataGenerator(
       rescale = 1./ 255,
       shear_range = 0.2,
       zoom_range = 0.2,
       horizontal_flip = True)

Y_datagen = ImageDataGenerator(
       rescale = 1./ 255)
       

X_generator = X_datagen.flow_from_directory(
               X,
               target_size = (img_width,img_height),
               batch_size = batch_size,
               class_mode = 'categorical')

Y_generator = Y_datagen.flow_from_directory(
               Y,
               target_size = (img_width,img_height),
               batch_size = batch_size,
               class_mode = 'categorical')


model = Sequential()
model.add(Conv2D(32,(3,3),input_shape = input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.summary()


model.add(Conv2D(64,(3,3),input_shape = input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Conv2D(32,(3,3),input_shape = input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(15))
model.add(Activation('softmax'))

model.summary()

model.compile(loss = 'binary_crossentropy',
              optimizer = 'adam',
              metrics=['accuracy'])


model.fit_generator(
    X_generator,
    steps_per_epoch = X_samples // batch_size,
    epochs = epochs,
    validation_data = Y_generator,
    validation_steps = Y_samples // batch_size)

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("plant_model8.h5")
print("Saved model to disk")


    
