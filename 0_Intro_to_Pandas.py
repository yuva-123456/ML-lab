import pandas as pd

data = [5, 10, 15, 20, 25, 30]
s = pd.Series(data)

print(s)
print(s.index)
print(s.values)
print(s.dtype)
print(s.shape)
print(s.size)

print(s.head(3))
print(s.tail(3))

print(s.sum())
print(s.mean())
print(s.min())
print(s.max())
print(s.std())

print(s.describe())
