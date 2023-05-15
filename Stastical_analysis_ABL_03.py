# Nikhil_Lanjewar_01

import numpy as np
import scipy.stats as stats
import statsmodels.api as sm

# Hypothesis Testing (t-test)
def t_test(sample1, sample2):
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)
    return t_statistic, p_value

# Linear Regression
def linear_regression(x, y):
    x = sm.add_constant(x)
    model = sm.OLS(y, x)
    results = model.fit()
    return results

# Hypothesis Testing (t-test) example
sample1 = [1, 2, 3, 4, 5]
sample2 = [6, 7, 8, 9, 10]
t_stat, p_val = t_test(sample1, sample2)
print("T-Statistic:", t_stat)
print("P-Value:", p_val)

# Linear Regression example
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 6]
results = linear_regression(x, y)
print(results.summary())
