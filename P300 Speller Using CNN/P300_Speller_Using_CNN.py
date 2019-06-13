import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D

model = Sequential()
model.add(Conv2D(10, kernel_size=(1, 64),
                 strides=(1,1),
                 activation='relu',
                 input_shape =(160, 64, 1)
                 ))
model.add(Conv2D(50, (13,1), activation='relu'))
model.add(Flatten())
model.add(Dense(100, activation='relu'))

model.add(Dense(2, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(),
              metrics=['accuracy'])


#save the model
keras.models.save_model(
    model = model,
    filepath = 'Models/Base_Model.h5',
    overwrite = True,
    include_optimizer=True
)

