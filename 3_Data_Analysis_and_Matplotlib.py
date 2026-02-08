import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

data = load_iris()
s = pd.Series(data.data[:, 0], name="Sepal Length")

print(s)
print(s.head())
print(s.tail())
print(s.mean())
print(s.median())
print(s.std())

plt.plot(s)
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.title("Sepal Length Analysis")
plt.show()
