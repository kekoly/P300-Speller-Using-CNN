
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import numpy as np
from collections import Counter

#Define Method to be called by app
#Takes arguments model name and file name
#Returns Prediction, and correct character
def feedMe(Model, file_name):

    if Model == 1:
        cnn_model = 'Subject_A_CNN.h5'
    elif Model == 2:
        cnn_model = 'Subject_B_CNN.h5'
    elif Model == 3:
        cnn_model = 'Subject_AB_CNN.h5'

    model_path = 'Models/'
    
    #Load desired model
    p300 = keras.models.load_model(model_path + cnn_model)
    #Load Grid
    grid = np.load('P300 Data/grid.npy')
 
    #Load desired file
    data = np.load(file_name)
    c_test = data.item().get('Signal')
    c_code = data.item().get('Code').astype(int)    
    c_index = data.item().get('Index')

    #added
    c_type = data.item().get('Type').astype(int)

    was = c_type * c_code
    was = Counter(was)        
    value1, value2, = was.most_common()[1:3]
    if value1[0] <= 6:
        tarcol = value1[0] - 1
    elif value1[0] >= 7:
        tarrow = value1[0] - 7
    if value2[0] <= 6:
        tarcol = value2[0] - 1
    elif value2[0] >= 6:
        tarrow = value2[0] - 7
    c_target = grid[tarrow,tarcol]


    #Voting counter
    count = []

    #predictions
    predictions = p300.predict(c_test)

    for y in range(288):
        if np.argmax(predictions[y]) == 1:
            count.append(c_code[y])

    c = Counter(count)
    lenght = len(c.most_common())

    for vote in range (0,lenght):
        value = c.most_common()[vote]
        if value[0] <= 6 and dir().count('col')==0:
            col = value[0] - 1
            continue
        elif value[0] >= 7 and dir().count('row')==0:
            row = value[0] - 7

    if dir().count('row')==0 or dir().count('col')==0:
        print(c.most_common())
        return 'Not Sure', c_target, c_index
    else:        

        print('This is Row: ', row, ' This is col: ', col)
        print('Majority Voting: ', c.most_common(), '\n')
        print('The prediction is: ', grid[row,col])
        print('\n\n')        
        return grid[row,col], c_target, c_index