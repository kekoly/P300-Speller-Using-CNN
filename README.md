# P300-Speller-Using-CNN

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
Tested on 17 characters each for Subject A and Subject B 

# Predictions
* Achieved P300 response recognition ratio of 92% for Subject A and 94% for subject B
* Achieved character recognition ratio of 88% on both Subjects
