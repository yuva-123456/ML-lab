import pandas as pd
import numpy as np

s = pd.Series([10, 15, 20, 25, 30])

def process(x):
    if x % 2 == 0:
        return x * 2
    else:
        return x + 5

print(s)
print(s.apply(process))
print(s.apply(lambda x: x ** 2))
print(s.apply(np.sqrt))
print(s.apply(str))
print(s.apply(len))
