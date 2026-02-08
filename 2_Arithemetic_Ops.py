import numpy as np
import math
from statistics import mean
from scipy import stats

a = np.array([10, 20, 30])
b = np.array([2, 4, 6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a % b)

print(mean(a))
print(math.sqrt(a[0]))
print(stats.gmean(a))
