import numpy as np

def col_mean(data):
    means = []
    total = 0

    for i in range(data.shape[1]):
        for j in range(data.shape[0]):
            total += data[j][i]
        means.append(total/data.shape[0])
        total = 0
    return means

def col_std(data):
    stds = []
    means = col_mean(data)

    for i in range(data.shape[1]):
        total = 0
        for j in range(data.shape[0]):
            total += ((data[j][i] - means[i]) ** 2)
        stds.append((total / data.shape[0]) ** (1/2))
    return stds

def col_min(data):
    mins = []

    for i in range(data.shape[1]):
        current_min = data[0][i]
        for j in range(data.shape[0]):
            if data[j][i] < current_min:
                current_min = data[j][i]
        mins.append(current_min)
    return mins

def col_max(data):
    maxes = []

    for i in range(data.shape[1]):
        current_max = data[0][i]
        for j in range(data.shape[0]):
            if data[j][i] > current_max:
                current_max = data[j][i]
        maxes.append(current_max)
    return maxes