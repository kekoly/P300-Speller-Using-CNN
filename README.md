# P300-Speller-Using-CNN
# But what is P300?
The P300 wave is an event-related potential (ERP) which can be recorded via electroencephalogram (EEG). The P300 wave is the cornerstone of Brain-Computer Interface research (BCI), which seeks a communication path between the human brain and an external device. Such systems allow people to communicate through direct measurements of brain activity, without requiring any movement [1], (Farwell and Donchin, 1988, Donchin et al., 2000). BCIs may be the only means of communication possible for people who are unable to communicate via conventional means because of severe motor disabilities. The wave corresponds to a positive deflection in voltage at a latency of about 300ms in the EEG. In other words, it means that after an event like a flashing light, a deflection in the signal should occur after 300ms.The presence, magnitude, topography, and time of this signal are used as metrics in decision making processes. The presence of a P300 wave signals where the user was focusing 300ms before its dectection. It looks more or less like the image below.

![](https://github.com/kekoly/P300-Speller-Using-CNN/blob/master/p300%20wave.jpg)

# How is P300 data recorded?
The user was presented with a 6 by 6 matrix of characters (see Figure below). The user’s task was to focus attention on characters in a word that was prescribed by the investigator (i.e., one character at a time). All rows and columns of this matrix were successively and randomly intensified at a rate of 5.7Hz. Two out of 12 intensifications of rows or columns contained the desired character (i.e., one particular row and one particular column). The responses evoked by these infrequent stimuli (i.e., the 2 out of 12 stimuli that did contain the desired character) are different from those evoked by the stimuli that did not contain the desired character and they are similar to the P300 responses previously reported (Farwell and Donchin, 1988, Donchin et al., 2000)

![](https://github.com/kekoly/P300-Speller-Using-CNN/blob/master/Grid.PNG)

[You can dowload this video to see it in action.](https://github.com/kekoly/P300-Speller-Using-CNN/blob/master/p300Video.mp4)

# The Dataset
For this Porject I used the Wadsworth BCI Dataset (P300 Evoked Potentials) Data Acquired Using BCI2000's P3 Speller Paradigm for BCI Competition III Subjects A & B. This dataset consists of collected signals (bandpass filtered from 0.1-60Hz and digitized at 240Hz) from two subjects in five sessions each. Each session consisted of a number of runs.  In each run, the subject focused attention on a series of characters. For each character epoch in the run, user display was as follows: the matrix was displayed for a 2.5 s period, and during this time each character had the same intensity (i.e., the matrix was blank). Subsequently, each row and column in the matrix was randomly intensified for 100ms (i.e., resulting in 12 different stimuli – 6 rows and 6 columns).  After intensification of a row/column, the matrix was blank for 75ms.  Row/column intensifications were block randomized in blocks of 12. The sets of 12 intensifications were repeated 15 times for each character epoch (i.e., any specific row/column was intensified 15 times and thus there were 180 total intensifications for each character epoch).  Each character epoch was followed by a 2.5 s period, and during this time the matrix was blank.  This period informed the user that this character was completed and to focus on the next character in the word that was displayed on the top of the screen (the current character was shown in parentheses just like in the video above). For the competition data set the recorded data has been converted into 4 Matlab *.mat files, one training (85 characters) and one test (100 characters) for each of the two subjects A and B.

# The Project
My goal with this project is to use the labeled training data (i.e., files Subject_A_Train.mat and Subject_B_Train.mat for subject A and B, respectively) to predict the character sequences in the test set (i.e., files Subject_A_Test.mat and Subject_B_Test.mat for subject A and B, respectively). The predictions are usually done with two separate networks for each character, but in an effort to create a more generalized network I also designed a single network trained ob both test subjects.

The model is based on the paper by [Cecotti and Graser](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5492691&isnumber=5692151) using BCI competiion III dataset II Subject A and Subject B

The design consists of 4 parts:
1.	The Preprocessing
2.	The training
3.	The testing
4.	Predictions

# Preprocessing
1. Extraction of data from matlab format
2. Filtering of Signal to cutoff not needed high frequency information
3. time window selection
4. averaging of character epochs

# Training
15 epochs per network 

# Testing
I couldnt find the labels for the 100 Test characters at first so took 17 out of the training set and used these for testing. I now have the labels for the 100 test set, I can now evaluate the accuraccy of the model. Will be updating soon... 

# Predictions
These results are using 17 characters as test set:
* Achieved P300 response recognition ratio of 92% for Subject A and 94% for subject B
* Achieved character recognition ratio of 88% on both Subjects
