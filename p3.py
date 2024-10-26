# check and drop

import pandas as pd

data=pd.read_csv("apple_Sep24.csv")
print(data)

print(data.isnull().sum())
data.dropna(inplace=True)
print(data.isnull().sum())
