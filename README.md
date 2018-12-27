# Background

Nowadays almost all possible human activity is computer related.
The more we spend time in front of the monitor, the more our everyday tasks become computer related.

Overall what this brings to the situation is known as long-term stress.

Available data set is introduced as WESAD (Wearable Stress and Affect Detection)
features physiological and motion data.
It includes observation on both a wrist- and chest-worn device, of 15
subjects during a lab study.

The following sensor modalities are included: blood volume pulse, electrocardiogram, electrodermal
activity, electromyogram, respiration, body temperature, and threeaxis acceleration.

# Goal

Create a system (web based preferable) which should accept input parameters and respond 
back with stress detection on early stages based on the prediction model created on existing data set.

This created system (or site) may be used by organizations who can have lab observations of patients.
By submitting results, they obtain the answer on stressed or affected conditions of patients.

# Data Source

An existing data set is provided as URL:
http://archive.ics.uci.edu/ml/machine-learning-databases/00465/

This URL points to a text file with an actual download file which is 1.2GB of size and extended to ~17 GB of raw data.

The data set is organized so that each subject has a folder (SX, where X = subject ID). 
Each subject folder contains the following files: 
- SX_readme.txt: contains information about the subject (SX) and information about data collection and data quality (if applicable) 
- SX_quest.csv: contains all relevant information to obtain ground truth, including the protocol schedule for SX and answers to the self-report questionnaires
- SX_respiban.txt: contains data from the RespiBAN device
- SX_E4_Data.zip: contains data from the Empatica E4 device
- SX.pkl: contains synchronised data and labels

17 subjects participated in the study. 
However, due to a sensor malfunction, data from two subjects (S1 and S12) had to be discarded.

# Approach

 - Understand data set structure and format
 - Explore and construct prediction model
 - Clean and transform data to a set eligible to construct prediction model
 - Create site with easy to use UI for input observable data
 - Integrate prediction model with website
 - Build and provide API
 
# Deliverable

This project aims to create source codes for website (simple UI)
 - Data manipulation scripts which will be used for initial data set cleanup and transformations
 - SQL database structure to store intermediate data along with prediction model
 - Source code for prediction model
 - Source code for web site
 - Deployment instructions and manuals
 
Ultimately provide deployed working site for demo purposes.

Currently cloud service providers such as **Amazon AWS** or **Google Cloud** may have free tier eligible solutions.
