#regression graph
import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv("apple_sep24.csv")
print(data)

feature=data[["qty"]]
target=data["price"]

model=LinearRegression()
model.fit(feature,target)
