import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([12, 25, 18, 30, 22, 28, 35])

def plot_graph(kind, title):
    plt.figure()
    if kind == "line":
        plt.plot(s)
    elif kind == "bar":
        plt.bar(s.index, s)
    elif kind == "scatter":
        plt.scatter(s.index, s)
    elif kind == "hist":
        plt.hist(s)
    elif kind == "box":
        plt.boxplot(s)
    plt.title(title)
    plt.show()

plot_graph("line", "Line Plot")
plot_graph("bar", "Bar Plot")
plot_graph("scatter", "Scatter Plot")
plot_graph("hist", "Histogram")
plot_graph("box", "Box Plot")
