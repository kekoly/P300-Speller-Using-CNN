# P300-Speller-Using-CNN
# But what is P300?
The P300 wave is an event-related potential (ERP) which can be recorded via electroencephalogram (EEG). The wave corresponds to a positive deflection in voltage at a latency of about 300ms in the EEG. In other words, it means that after an event like a flashing light, adeflection in the signal should occur after 300ms.The presence, magnitude, topography, and time of this signal are used as metrics in decision making processes. The presence of a P300 wave signals where the user was focusing 300ms before its dectection.

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
