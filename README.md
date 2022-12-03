# DS_MQTT
 18668 Individual Project on IoT Attack Detection

# Data
[https://www.kaggle.com/datasets/cnrieiit/mqttset?resource=download](https://www.kaggle.com/datasets/cnrieiit/mqttset?resource=download)

# Traditional Approach
1. Protocol Parsing and Strict Validations
    - Husnain M, Hayat K, Cambiaso E, Fayyaz UU, Mongelli M, Akram H, Ghazanfar Abbas S, Shah GA. Preventing MQTT Vulnerabilities Using IoT-Enabled Intrusion Detection System. Sensors (Basel). 2022 Jan 12;22(2):567. doi: 10.3390/s22020567. PMID: 35062536; PMCID: PMC8779830.
    - Require a lot of human effort to define the validation rules.
    - Risk of getting reverse-engineered by malicious users

# Previous ML Approach
1. modes: tensorflow nn + DecisionTree + NaiveBayes
2. Oversampling before splitting # very biased
4. No feature scaling


# Plan
1. Preprocess
    - combine datasets
    - drop less useful features (following the original paper's approach)
    - impute null values
    - encode nomial and categorical features
    - encode label
    - Train/Test Split 
    - Feature Scaling
    - Resampling
        - Oversampling, SMOTE
        - Hybrid 
2. sklearn ml
    - random forest
3. xgboost
4. tensorflow nn

# Results

| Model | Resampling | Accuracy | F1-Brute Force | F1-Flood | F1-Legitimate | F1-Malaria | F1-Malformed | F1-Slowite|
|--|--|--|--|--|--|--|--|--|
|RandomForest | None | 0.9968 | 0.7427| 0.6423| 0.9987| 0.8765| 0.6716| 0.7144|
|RandomForest | RandomUnder+RandomOver | 0.9849 | 0.7399| 0.6263| 0.9928| 0.5766| 0.667| 0.7092|
|RandomForest | RandomUnder+SMOTE | 0.9936 | 0.7491| 0.635| 0.9972| 0.7487| 0.6601| 0.7035|
|RandomForest | NearMiss+SMOTE | 0.9895 | 0.7498| 0.635| 0.9951| 0.7486| 0.1702| 0.7035|
|Xgboost | None | 0.9967 | 0.7539| 0.6397| 0.9987| 0.8779| 0.656| 0.7065|
|Xgboost | RandomUnder+RandomOver | 0.9849 | 0.7404| 0.6296| 0.9927| 0.5766| 0.6593| 0.7156 |
|Xgboost | RandomUnder+SMOTE| 0.9850 | 0.7539| 0.6347| 0.9928| 0.5766| 0.6616| 0.7139 | 
|Xgboost | NearMiss+SMOTE| 0.9806 | 0.7549| 0.6296| 0.9905| 0.5302| 0.3358| 0.7111 |
| Neural Network| None | 0.9954 | 0.6463| 0.6347| 0.9979| 0.8326| 0.4798| 0.5594 |
| Neural Network| RandomUnder+RandomOver | 0.9953 | 0.6239| 0.6397| 0.9979| 0.8326| 0.4887| 0.4545 |
| Neural Network| RandomUnder+SMOTE | 0.9953 | 0.6245| 0.63| 0.9979| 0.8326| 0.4882| 0.4545|
| Neural Network| NearMiss+SMOTE | 0.9386 | 0.624| 0.6397| 0.9683| 0.8327| 0.0103| 0.4545 |



# Findings:
1. Oversampling alone overfits terribly
2. Undersampling lose too much information due to the huge gap between number of samples
3. NearMiss Method makes random forest overfit class5

# Citation

Vaccari, I.; Chiola, G.; Aiello, M.; Mongelli, M.; Cambiaso, E. MQTTset, a New Dataset for Machine Learning Techniques on MQTT. Sensors 2020, 20, 6578. https://doi.org/10.3390/s20226578

