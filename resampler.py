from collections import Counter


def class_distribution(labels):
    return sorted(Counter(labels).items())


def random_oversample(x_train, y_train, strategy='auto'):
    from imblearn.over_sampling import RandomOverSampler

    ros = RandomOverSampler(sampling_strategy=strategy, random_state=42)
    x_resampled, y_resampled = ros.fit_resample(x_train, y_train)
    return x_resampled, y_resampled


