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

# Findings:
1. Oversampling alone overfits terribly
2. Undersampling lose too much information due to the huge gap between number of samples
3. NearMiss Method makes random forest overfit class5

# Citation

Vaccari, I.; Chiola, G.; Aiello, M.; Mongelli, M.; Cambiaso, E. MQTTset, a New Dataset for Machine Learning Techniques on MQTT. Sensors 2020, 20, 6578. https://doi.org/10.3390/s20226578

