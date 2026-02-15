import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

data = {
    "TV": [230,44,17,151,180,8,57,120,240,100],
    "Radio": [37,39,45,41,10,43,20,30,50,40],
    "Newspaper": [69,45,69,58,58,23,11,35,80,60],
    "Sales": [22.1,10.4,9.3,18.5,12.9,7.2,11.8,13.2,25.4,14.7]
}

df = pd.DataFrame(data)

print(df.head())

x = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(f"Training set: {x_train.shape}")
print(f"Testing set: {x_test.shape}")

print("Lineer Regresyon Modeli Eğitiliyor...")
model = LinearRegression()
model.fit(x_train, y_train)

print("Model eğitildi!")
print(f"Model katsayıları: {model.coef_}")
print(f"Model intercept: {model.intercept_}")

y_pred = model.predict(x_test)

for gerçek, tahmin in zip(y_test, y_pred):
    print(f"Gerçek: {gerçek}, Tahmin: {tahmin:.2f}")

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

plt.scatter(y_test, y_pred)
plt.xlabel("Gerçek Değerler")   
plt.ylabel("Tahmin Edilen Değerler")
plt.title("Gerçek vs Tahmin Edilen Değerler")   
plt.grid()
plt.show()
plt.savefig("gercek_vs_tahmin.png")