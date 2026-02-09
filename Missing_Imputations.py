import pandas as pd
import numpy as np

s = pd.Series([10, np.nan, 30, np.nan, 50])

print(s)

print(s.isna())
print(s.fillna(0))
print(s.ffill())
print(s.bfill())
print(s.mean())
print(s.fillna(s.mean()))
