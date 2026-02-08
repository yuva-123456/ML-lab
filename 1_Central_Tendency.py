import pandas as pd

data = [10, 20, 20, 30, 40]
s = pd.Series(data)

mean = s.mean()
median = s.median()
mode = s.mode()[0]
variance = s.var()
std_dev = s.std()

print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
print("Variance =", variance)
print("Standard Deviation =", std_dev)
