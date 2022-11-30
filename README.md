# DS_MQTT
 18668 Individual Project on IoT Attack Detection

# Data
[https://www.kaggle.com/datasets/cnrieiit/mqttset?resource=download](https://www.kaggle.com/datasets/cnrieiit/mqttset?resource=download)


# Previous Approach
1. modes: tensorflow nn + DecisionTree + NaiveBayes
2. Oversampling before splitting # very biased
3. Kept a lot of bad features (large number of null values, bad distribution)
4. No feature scaling


# Plan
1. Preprocess
    - combine datasets
    - drop less useful features
    - impute null values
    - encode nomial and categorical features
    - encode label
    - Train/Test Split 
    - Feature Scaling
    - Resampling
        - Oversampling
        - SMOTE
2. sklearn ml
    - random forest
3. xgboost
4. tensorflow nn

