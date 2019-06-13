import keras
import numpy as np

#General Variables
batch_size = 128
epochs = 15
num_classes = 2
img_rows, img_cols = 160, 64

#Load Data
x_train = np.load('P300 Data/ab_signal_train.npy')
x_test = np.load('P300 Data/a_signal_test.npy')
y_train = np.load('P300 Data/ab_type_train.npy').astype(int)
y_test = np.load('P300 Data/a_type_test.npy').astype(int)
a_code_test = np.load('P300 Data/a_code_test.npy').astype(int)
xb_test = np.load('P300 Data/b_signal_test.npy')
yb_test = np.load('P300 Data/a_type_test.npy').astype(int)

p300 = keras.models.load_model('Models/Base_Model.h5')

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
yb_test = keras.utils.to_categorical(yb_test, num_classes)

p300.fit(x_train, y_train, validation_split = 0.02941176, epochs = epochs, verbose = 1)


score = p300.evaluate(x_test, y_test, verbose = 1)
print("\nTest Set A Validation Results-> %s: %.2f%%" % (p300.metrics_names[1], score[1]*100) ,"%s: %.2f%%" % (p300.metrics_names[0], score[0]*100) )

score = p300.evaluate(xb_test, yb_test, verbose = 1)
print("\nTest Set B Validation Results-> %s: %.2f%%" % (p300.metrics_names[1], score[1]*100) ,"%s: %.2f%%" % (p300.metrics_names[0], score[0]*100) )

#save the model
keras.models.save_model(
    model = p300,
    filepath = 'Models/Subject_AB_CNN.h5',
    overwrite = True,
    include_optimizer=True
)
