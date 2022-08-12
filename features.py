import numpy as np
import pandas as pd
from cesium.features import graphs as f_engine
from scipy.signal import find_peaks

"""===== Derived Features ====="""
def AUC_ratio(d):
    height = d['elevation']
    count = d['intensity']

    idx_1 = (height > -1) & (height < 0)
    idx_2 = (height > -10) & (height < -1)
    
    
    AUC_0_1 = np.trapz(count[idx_1])
    AUC_1_10 = np.trapz(count[idx_2])
    
    return AUC_0_1 / AUC_1_10
    
def Peak_Count(d):
    height = d['elevation']
    count = d['intensity']

    idx_peaks = find_peaks(count, prominence=16)[1]['prominences']
    
    return len(idx_peaks)

def max_slope(d):
    height = d['elevation']
    count = d['intensity']
    
    return f_engine.max_slope(height,count)

def median_absolute_deviation(d):
    height = d['elevation']
    count = d['intensity']
    
    return f_engine.median_absolute_deviation(count)

"""====== Statistical Shape Features ====="""

def n_bar(count):
    n = np.arange(1,len(count)+1)
    sum_yn = np.sum(n*count)
    return sum_yn / np.sum(count)

def moment(count, m):
    n_minus_nbar = count - n_bar(count)

    return np.sum(count * n_minus_nbar**m) / np.sum(count)

def mode(d):
    height = d['elevation']
    count = d['intensity']
    
    peak = np.where(count == count.max())[0][0]
    return peak

def Mean(d):
    height = d['elevation']
    count = d['intensity']
    
    n = np.arange(1,len(count)+1)
    return np.sum(n*count) / np.sum(count)

def mean(count):
    n = np.arange(1,len(count)+1)
    return np.sum(n*count) / np.sum(count)

def skewness(d):
    height = d['elevation']
    count = d['intensity']
    
    return moment(count,3) / moment(count,2)**1.5

def kurtosis(d):
    height = d['elevation']
    count = d['intensity']
    
    return moment(count,4) / moment(count,2)**2

def sum_squares(count):
    n = np.arange(1,len(count)+1)
    return np.sum(n**2 * count)

def variance(d):
    height = d['elevation']
    count = d['intensity']
    
    n = np.arange(1,len(count)+1)

    mean_square = sum_squares(count) / np.sum(count)
    return mean_square - mean(count)**2

def stdev(d):
    return np.sqrt(variance(d))

def pearson_skewness1(d):
    height = d['elevation']
    count = d['intensity']
    
    return (mean(count) - mode(d)) / stdev(d)

def third_quartile(d):
    height = d['elevation']
    count = d['intensity']

    return np.quantile(count, .75)

def computeFeatures(waveforms):
    features = {
        "Kurtosis": [kurtosis(d) for d in waveforms.values()],
        "Std Dev": [stdev(d) for d in waveforms.values()],
        "Mean": [Mean(d) for d in waveforms.values()],
        "AUC Ratio": [AUC_ratio(d) for d in waveforms.values()],
        "Pearson 1": [pearson_skewness1(d) for d in waveforms.values()],
        "Q3": [third_quartile(d) for d in waveforms.values()],
        "M.A.D.": [median_absolute_deviation(d) for d in waveforms.values()],
        "Skewness": [skewness(d) for d in waveforms.values()],
        "MaxSlope": [max_slope(d) for d in waveforms.values()],
        "# Peaks": [Peak_Count(d) for d in waveforms.values()]
    }
    
    return pd.DataFrame.from_dict(features, orient='index', columns=waveforms.keys())