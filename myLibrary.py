import numpy as np

def min_max_scaler(data, newmin, newmax):
    min_values = np.min(data, axis=0)
    max_values = np.max(data, axis=0)
    return (newmin + ((data - min_values) / (max_values - min_values)) * (newmax - newmin))

def z_score_standardizer(data):
    return ((data-np.mean(data, axis=0)) / np.std(data, axis=0))

def train_test_split(data, train_p, seed):
    np.random.seed(seed)

    indices = np.arange(len(data))
    np.random.shuffle(indices)
    shuffled = data[indices]
    
    if train_p > 1:
        train_p /= 100
    split_pos = int(len(data) * train_p)

    train = shuffled[:split_pos]
    test = shuffled[split_pos:]

    return train,test