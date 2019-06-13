
#Libraries
import scipy.io as sio
from scipy import signal
import numpy as np
from sklearn import preprocessing
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from keras import backend as K


#Load Subject A Raw Data
Subject_A_Train_Raw = sio.loadmat("C:/Users/Greg/OneDrive - Salem State University/2018 Fall CSC521/Files/Subject_A_Train.mat")
a_signal_raw = Subject_A_Train_Raw['Signal'].astype('float32')
a_flash_raw = Subject_A_Train_Raw['Flashing'].astype('float32')
a_type_raw = Subject_A_Train_Raw['StimulusType'].astype('int')
a_code_raw = Subject_A_Train_Raw['StimulusCode'].astype('int')

#Filter the Data Using Butterworth bandpass filter of 0.1Hz to 20Hz
sos = signal.butter(4,[0.1, 20],'bandpass', output='sos',fs=240)
a_filtered = signal.sosfilt(sos,a_signal_raw)


#choose time window, 667ms after stimulus onset
# 85 x 7794 x 64 - Input Shape
# 85 x 4320 x 160 x 64 - Output Shape
a_window = np.zeros((85,4320,160,64),'float32')

for character in range(85):
    print('Choosing Time Window for Character epoch :', character)
    intensification = 0
    for sample in range(7560):
        if a_flash_raw[character,sample] == 1:            
            for time in range(160):
                a_window[character,intensification,time] = a_filtered[character,sample + time,]
            intensification += 1

#Stimulus Code to Signal Window Shape in order to Average  Signal
#85 x 7794 - input shape
#85 x 4320 - output shape, there are only 4320 Flashes per epoch
a_code_4320= np.zeros((85,4320),int)

for character in range(85):
    new_index = 0
    for code in range(7560):       
        if a_flash_raw[character,code]==1:          
            a_code_4320[character,new_index] = a_code_raw[character,code].astype(int)           
            new_index += 1     #This goes to 4320       

#Average Signal
#85 x 4320 x 160 x 64 input shape
#85 x 12 x 24 x 160 x 64 - output Shape
a_avgd = np.zeros((85,12,24,160,64))

for c in range(85):
    print('Averaging Character epoch :', c)    
    sample_number = 0
    for iteration in range(15):
        for rowcol in range(12):
            rowcol_index = a_code_4320[c,sample_number].astype(int) - 1           
            for flash_sample in range(24):                
                a_avgd[c, rowcol_index, flash_sample] += a_window[c,sample_number]
                sample_number += 1      #This goes to 4320   
a_avgd = a_avgd/15 

#Scale Signal range -1 to 1
#85 x 12 x 24 x 160 x 64 - input shape
#85 x 288 x 160 x 64 - output shape
print('Scaling...')
a_avgd = np.reshape(a_avgd,(3916800,64))
a_scaled = preprocessing.maxabs_scale(a_avgd)
a_scaled = np.reshape(a_scaled,(85,288,160,64))


#Average stimulus code to match new signal and reshape for network input
#85 x 4320 - input shape
#85 x 288, - output shape
a_code = np.zeros((85,12,24),'int')

for c in range(85):
    print('Reshaping rows and columns labels for character:', c)
    sample_number = 0 #This goes to 4320
    for iteration in range(15):
        for rowcol in range(12):
            rc_index = a_code_4320[c,sample_number].astype(int) - 1           
            for flash_sample in range(24):
                a_code[c,rc_index,flash_sample] += a_code_4320[c,sample_number]
                sample_number += 1
a_code = a_code/15
a_code = np.reshape(a_code,(85,288))


#Stimulus Type to Shape 85 x 4320
#85 x 7794 - input shape
#85 x 4320 - output shape
a_type_4320 = np.zeros((85,4320),'int')
for character in range(85):
    new_index = 0
    for type in range(7560):       
        if a_flash_raw[character,type]==1:          
            a_type_4320[character,new_index] = a_type_raw[character,type].astype(int)
            new_index += 1

#Average stimulus Type
#85 x 4320 - input shape
#85 x 288, - output shape
a_type = np.zeros((85,12,24),'int')
for c in range(85):
    sample_number = 0
    print("Reshaping stimulus type for character : ", c)
    for iteration in range(15):
        for rowcol in range(12):
            rc_index = a_code_4320[c,sample_number].astype(int) - 1
            for flash_sample in range(24):
                a_type[c,rc_index,flash_sample] += a_type_4320[c,sample_number].astype(int)
                sample_number += 1

a_type = a_type/15
a_type = np.reshape(a_type,(85,288))

#Shuffle data as it is now in order by row colunm index
print('Shuffling...')
a_scaled, a_type, a_code = shuffle(a_scaled, a_type,a_code)

#Split data between 80% Training and 20% Testing
print('Splitting...')
a_scaled = np.reshape(a_scaled,(24480,160,64))
a_type = np.reshape(a_type,(24480,))
a_code = np.reshape(a_code,(24480,))

x_train, x_test, y_train, y_test = train_test_split(
    a_scaled, a_type, train_size=.8, test_size=.2, shuffle=False)

a_code_train, a_code_test = a_code[:19584], a_code[19584:]



#format data as input tensor shape
img_rows, img_cols = 160, 64
if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

#Save data
print('Saving data for Subject A...')
np.save('P300 Data/a_signal_train.npy',x_train)
np.save('P300 Data/a_signal_test.npy',x_test)
np.save('P300 Data/a_type_train.npy',y_train)
np.save('P300 Data/a_type_test.npy',y_test)
np.save('P300 Data/a_code_train.npy',a_code_train)
np.save('P300 Data/a_code_test.npy',a_code_test)

#Save test data individually per character for app

x_test = x_test.reshape(17, 288, 160, 64, 1)
y_test = y_test.reshape(17,288)
a_code_test = a_code_test.reshape(17,288)

for c in range(1,18):
    #Autonaming characters 1-17
    file_name = 'A_Test_Character_' + str(c)

    #Extract one character epoch signal, type, and code   
    a_test = x_test[c-1]
    a_test_type = y_test[c-1]
    a_code_c = a_code_test[c-1]

    joint = {'Signal' : a_test, 'Type': a_test_type, 'Code': a_code_c, 'Index' : c}   

    print('Saving Test data for Subject A...', c)
    np.save('Test Data/'+ file_name, joint)

#Load Subject B Raw Data
print('\n\nNow processing Subject B data...\n\n')
Subject_B_Train_Raw = sio.loadmat("C:/Users/Greg/OneDrive - Salem State University/2018 Fall CSC521/Files/Subject_B_Train.mat")
b_signal_raw = Subject_B_Train_Raw['Signal'].astype('float32')
b_flash_raw = Subject_B_Train_Raw['Flashing'].astype('float32')
b_type_raw = Subject_B_Train_Raw['StimulusType'].astype('int')
b_code_raw = Subject_B_Train_Raw['StimulusCode'].astype('int')

#Filter the Data Using Butterworth bandpass filter of 0.1Hz to 20Hz
sos = signal.butter(4,[0.1, 20],'bandpass', output='sos',fs=240)
b_filtered = signal.sosfilt(sos,b_signal_raw)


#choose time window, 667ms after stimulus onset
# 85 x 7794 x 64 - Input Shape
# 85 x 4320 x 160 x 64 - Output Shape
b_window = np.zeros((85,4320,160,64),'float32')

for character in range(85):
    print('Choosing Time Window for Character epoch :', character)
    intensification = 0
    for sample in range(7560):
        if b_flash_raw[character,sample] == 1:            
            for time in range(160):
                b_window[character,intensification,time] = b_filtered[character,sample + time,]
            intensification += 1

#Stimulus Code to Signal Window Shape in order to Average  Signal
#85 x 7794 - input shape
#85 x 4320 - output shape, there are only 4320 Flashes per epoch
b_code_4320= np.zeros((85,4320),int)

for character in range(85):
    new_index = 0
    for code in range(7560):       
        if b_flash_raw[character,code]==1:          
            b_code_4320[character,new_index] = b_code_raw[character,code].astype(int)           
            new_index += 1     #This goes to 4320       

#Average Signal
#85 x 4320 x 160 x 64 input shape
#85 x 12 x 24 x 160 x 64 - output Shape
b_avgd = np.zeros((85,12,24,160,64))

for c in range(85):
    print('Averaging Character epoch :', c)    
    sample_number = 0
    for iteration in range(15):
        for rowcol in range(12):
            rowcol_index = b_code_4320[c,sample_number].astype(int) - 1           
            for flash_sample in range(24):                
                b_avgd[c, rowcol_index, flash_sample] += b_window[c,sample_number]
                sample_number += 1      #This goes to 4320   
b_avgd = b_avgd/15 

#Scale Signal range -1 to 1
#85 x 12 x 24 x 160 x 64 - input shape
#85 x 288 x 160 x 64 - output shape
print('Scaling...')
b_avgd = np.reshape(b_avgd,(3916800,64))
b_scaled = preprocessing.maxabs_scale(b_avgd)
b_scaled = np.reshape(b_scaled,(85,288,160,64))


#Average stimulus code to match new signal and reshape for network input
#85 x 4320 - input shape
#85 x 288, - output shape
b_code = np.zeros((85,12,24),'int')

for c in range(85):
    print('Reshaping row and columns labels for character:', character)
    sample_number = 0 #This goes to 4320
    for iteration in range(15):
        for rowcol in range(12):
            rc_index = b_code_4320[c,sample_number].astype(int) - 1           
            for flash_sample in range(24):
                b_code[c,rc_index,flash_sample] += b_code_4320[c,sample_number]
                sample_number += 1
b_code = b_code/15
b_code = np.reshape(b_code,(85,288))


#Stimulus Type to Shape 85 x 4320
#85 x 7794 - input shape
#85 x 4320 - output shape
b_type_4320 = np.zeros((85,4320),'int')
for character in range(85):
    new_index = 0
    for type in range(7560):       
        if b_flash_raw[character,type]==1:          
            b_type_4320[character,new_index] = b_type_raw[character,type].astype(int)
            new_index += 1

#Average stimulus Type
#85 x 4320 - input shape
#85 x 288, - output shape
b_type = np.zeros((85,12,24),'int')
for c in range(85):
    sample_number = 0
    print("Reshaping stimulus type for character : ", c)
    for iteration in range(15):
        for rowcol in range(12):
            rc_index = b_code_4320[c,sample_number].astype(int) - 1
            for flash_sample in range(24):
                b_type[c,rc_index,flash_sample] += b_type_4320[c,sample_number].astype(int)
                sample_number += 1

b_type = b_type/15
b_type = np.reshape(b_type,(85,288))

#Shuffle data as it is now in order by row colunm index
print('Shuffling...')
b_scaled, b_type, b_code = shuffle(b_scaled, b_type,b_code)

#Split data between 80% Training and 20% Testing
print('Splitting...')
b_scaled = np.reshape(b_scaled,(24480,160,64))
b_type = np.reshape(b_type,(24480,))
b_code = np.reshape(b_code,(24480,))

x_train, x_test, y_train, y_test = train_test_split(
    b_scaled, b_type, train_size=.8, test_size=.2, shuffle=False)

b_code_train, b_code_test = b_code[:19584], b_code[19584:]


#format data as input tensor shape
img_rows, img_cols = 160, 64
if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

#Save data
print('Saving data for Subject B...')
np.save('P300 Data/b_signal_train.npy',x_train)
np.save('P300 Data/b_signal_test.npy',x_test)
np.save('P300 Data/b_type_train.npy',y_train)
np.save('P300 Data/b_type_test.npy',y_test)
np.save('P300 Data/b_code_train.npy',b_code_train)
np.save('P300 Data/b_code_test.npy',b_code_test)

#Save test data individually per character for app

x_test = x_test.reshape(17, 288, 160, 64, 1)
y_test = y_test.reshape(17,288)
b_code_test = b_code_test.reshape(17,288)

for c in range(1,18):
    #Autonaming characters 1-17
    file_name = 'B_Test_Character_' + str(c)

    #Extract one character epoch signal, type, and code   
    b_test = x_test[c-1]
    b_test_type = y_test[c-1]
    b_code_c = b_code_test[c-1]

    joint = {'Signal' : b_test, 'Type': b_test_type, 'Code': b_code_c, 'Index' : c}   

    print('Saving Test data for Subject B...', c)
    np.save('Test Data/'+ file_name, joint)

#Combine Subject's A and B data
b_train =np.load('P300 Data/b_signal_train.npy')
b_type = np.load('P300 Data/b_type_train.npy')
a_train =np.load('P300 Data/a_signal_train.npy')
a_type = np.load('P300 Data/a_type_train.npy')


ab_signal = np.concatenate((a_train, b_train))
ab_type = np.concatenate((a_type, b_type))


#Shuffle data as it is now in order Subject A and then Subject B
print('Shuffling...')
ab_signal, ab_type = shuffle(ab_signal, ab_type)

#Save combined Data
print('Saving combined data...')
np.save('P300 Data/ab_signal_train.npy',ab_signal)
np.save('P300 Data/ab_type_train.npy',ab_type)

#Make Grid
screen=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','_')
grid = np.reshape(screen,(6,6))
np.save('P300 Data/grid.npy',grid)

