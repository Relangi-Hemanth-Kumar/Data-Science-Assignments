# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 00:45:08 2023

@author: HEMANTH
"""

import scipy.stats as stats
import numpy as np
# Sample data
sample_mean = 200  # Average weight of the sample
sample_std_dev = 30  # Standard deviation of the sample
sample_size = 2000  # Sample size
degrees_of_freedom = sample_size - 1
from scipy import stats
from scipy.stats import t
# for 94% confidence interval
ci_min,ci_max = stats.t.interval(0.94,df=degrees_of_freedom, loc = sample_mean, scale = sample_std_dev/np.sqrt(sample_size))
print(ci_min,ci_max)
# for 98% confidence interval
ci_min,ci_max = stats.t.interval(0.98,df=degrees_of_freedom, loc = sample_mean, scale = sample_std_dev/np.sqrt(sample_size))
print(ci_min,ci_max)
# for 96% confidence interval
ci_min,ci_max = stats.t.interval(0.96,df=degrees_of_freedom, loc = sample_mean, scale = sample_std_dev/np.sqrt(sample_size))
print(ci_min,ci_max)
