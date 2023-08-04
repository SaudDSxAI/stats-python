import numpy as np
from scipy import stats

#Balanced point
def mean(list):
    value = np.mean(list)
    return value

#The middle value
def median(list):
    value = np.median(list)
    return value

#The most friquent value
def mod(list):
    value = stats.mode(list, keepdims=True)
    return value[0]

#The arithmetic mean
def average(list):
    value = np.average(list)
    return value

#The variance
def variance(list):
    value = np.var(list)
    return value

#The std-deviatio
def std_deviation(list):
    value = np.std(list)
    return value

#range 
def range(list):
    value = np.ptp(list)
    return value

#A list
list = [1,1,2,2,2,2,2,3,4,5,6,7,8,9]

Mean = mean(list)
Median = median(list)
Mod  = mod(list)
Average = average(list)
Variance = variance(list)
Std_deviation = std_deviation(list)
Range = range(list)

print("Mean = ",Mean)
print("Median = ",Median)
print("Mod = ",Mod)
print("Average = ",Average)
print("variance = ",Variance)
print("STD_deviation = ",Std_deviation)
print("Range = ",Range)



