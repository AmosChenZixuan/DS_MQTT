from collections import Counter


def class_distribution(labels):
    return sorted(Counter(labels).items())


# Undersampling
def random_undersample(x_train, y_train, strategy='auto'):
    from imblearn.under_sampling import RandomUnderSampler
    rus = RandomUnderSampler(sampling_strategy=strategy, random_state=42)
    x_resampled, y_resampled = rus.fit_resample(x_train, y_train)
    return x_resampled, y_resampled


def near_miss(x_train, y_train, strategy='auto'):
    from imblearn.under_sampling import NearMiss

    nm = NearMiss(sampling_strategy=strategy)
    x_resampled, y_resampled = nm.fit_resample(x_train, y_train)
    return x_resampled, y_resampled


# Oversampling
def random_oversample(x_train, y_train, strategy='auto'):
    from imblearn.over_sampling import RandomOverSampler

    ros = RandomOverSampler(sampling_strategy=strategy, random_state=42)
    x_resampled, y_resampled = ros.fit_resample(x_train, y_train)
    return x_resampled, y_resampled

def smote(x_train, y_train, strategy='auto'):
    from imblearn.over_sampling import SMOTE
    sm = SMOTE(sampling_strategy=strategy, random_state=42)
    x_resampled, y_resampled = sm.fit_resample(x_train, y_train)
    return x_resampled, y_resampled