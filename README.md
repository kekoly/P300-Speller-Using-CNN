# P300 Speller Using CNN

## The Project
In short, this convolutuional network takes in electroencephalogram scans of brain activity and outputs which character from a set the subject was focusing on at the time when the scan was collected.



### Insert gif here


My goal with this project is to use the labeled training data to predict the character sequences in the test set. The predictions are usually done with two separate networks for each character, but in an effort to create a more generalized network I also designed a single network trained on both test subjects.

The model is based on the paper by [Cecotti and Graser](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5492691&isnumber=5692151) using BCI competiion III dataset II Subject A and Subject B

## But what is P300?
The P300 wave is an event-related potential (ERP) which can be recorded via electroencephalogram (EEG). The P300 wave is the cornerstone of Brain-Computer Interface research (BCI), which seeks a communication path between the human brain and an external device. The wave corresponds to a positive deflection in voltage at a latency of about 300ms in the EEG. The presence of a P300 wave signals where the user was focusing 300ms before its dectection. It looks more or less like the image below.

![](https://github.com/kekoly/P300-Speller-Using-CNN/blob/master/p300%20wave.jpg)

## How is P300 data recorded?
The user was presented with a 6 by 6 matrix of characters (see Figure below). The user’s task was to focus attention on characters in a word that was prescribed by the investigator (i.e., one character at a time). All rows and columns of this matrix were successively and randomly intensified at a rate of 5.7Hz. Two out of 12 intensifications of rows or columns contained the desired character (i.e., one particular row and one particular column). The responses evoked by these infrequent stimuli (i.e., the 2 out of 12 stimuli that did contain the desired character) are different from those evoked by the stimuli that did not contain the desired character and they are similar to the P300 responses previously reported (Farwell and Donchin, 1988, Donchin et al., 2000)

![](https://github.com/kekoly/P300-Speller-Using-CNN/blob/master/Grid.PNG)

[You can watch this video to see it in action.](https://github.com/kekoly/P300-Speller-Using-CNN/blob/master/P300%20recording.gif)

## The Data set
For this Porject I used the Wadsworth BCI Dataset (P300 Evoked Potentials) Data Acquired Using BCI2000's P3 Speller Paradigm for BCI Competition III Subjects A & B. This dataset consists of collected signals (bandpass filtered from 0.1-60Hz and digitized at 240Hz) from two subjects in five sessions each. For the competition data set the recorded data has been converted into 4 Matlab *.mat files, one training (85 characters) and one test (100 characters) for each of the two subjects A and B.

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

### Training
15 epochs per network 

### Testing
I couldnt find the labels for the 100 Test characters at first so took 17 out of the training set and used these for testing. I now have the labels for the 100 test set, I can now evaluate the accuraccy of the model. Will be updating soon... 

### Predictions
These results are using 17 characters as test set:
* Achieved P300 response recognition ratio of 92% for Subject A and 94% for subject B
* Achieved character recognition ratio of 88% on both Subjects
