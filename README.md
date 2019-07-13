# P300 Speller

This is an implementation of a convolutional neural network, that uses electroencephalogram scans of a subject's brain activity to predict which character from a given set the subject was focusing on at the time the scans were collected.

The model was implemented using Keras, and it's based on the [paper by Cecotti and Graser](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5492691&isnumber=5692151).

## P300
The P300 wave is an event-related potential (ERP) which can be recorded via electroencephalogram (EEG). The wave corresponds to a positive deflection in voltage at a latency of about 300ms in the EEG. The presence of a P300 wave signals where the user was focusing 300ms before its dectection. It looks more or less like the image below.

![](https://github.com/kekoly/P300-Speller-Using-CNN/blob/master/p300%20wave.jpg)

To collect the data, the user is presented with a 6 by 6 matrix of characters (see Figure below). The user’s task was to focus attention on characters in a word that was prescribed by the investigator, one character at a time. All rows and columns of this matrix were successively and randomly intensified at a rate of 5.7Hz. Two out of 12 intensifications of rows or columns contained the desired character (i.e., one particular row and one particular column). The responses evoked by these infrequent stimuli are different from those evoked by the stimuli that did not contain the desired character and they are similar to the P300 responses previously reported.

![recording the data](https://github.com/kekoly/P300-Speller-Using-CNN/blob/master/P300%20recording.gif)

### Data set
The Wadsworth BCI Dataset was used to train the model. This dataset consists of bandpass filtered signals from 0.1-60Hz and digitized at 240Hz, from two subjects in five sessions each. 

The data has been converted into 4 Matlab *.mat files, one training (85 characters) and one test (100 characters) for each of the two subjects.

## The Process
The design consists of 4 parts:
1.	The Preprocessing
2.	The training
3.	The testing
4.	Predictions

### Preprocessing
1. Extraction of data from matlab format
2. Filtering of Signal to cutoff not needed high frequency information
3. time window selection
4. averaging of character epochs

### Training and Testing
Each network was trained for 15 epochs.

17 charcters were extracted from the training and were used as the test set.

### Predictions
Test set results:
* Achieved P300 response recognition ratio of 92% for Subject A and 94% for subject B
* Achieved character recognition ratio of 88% on both Subjects
