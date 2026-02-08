import pandas as pd

data = [
    ['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
    ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
    ['Rainy','Cold','High','Strong','Warm','Change','No'],
    ['Sunny','Warm','High','Strong','Cool','Change','Yes']
]

df = pd.DataFrame(data)
hypothesis = ['0'] * 6

for i in range(len(df)):
    if df.iloc[i, -1] == 'Yes':
        for j in range(6):
            if hypothesis[j] == '0':
                hypothesis[j] = df.iloc[i, j]
            elif hypothesis[j] != df.iloc[i, j]:
                hypothesis[j] = '?'

print(hypothesis)
