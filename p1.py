#creating graph
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("apple_sep24.csv")
print(data)

x=data[["qty"]]
y=data["price"]

plt.scatter(x,y,color="red")
plt.xlabel("qty")
plt.ylabel("price")
plt.show()