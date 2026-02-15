import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data_classification = {
    "Age": [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    "Income": [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000],
    "Purchased": [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
}
df_classification = pd.DataFrame(data_classification)

print(df_classification.head())

x_cls = df_classification[["Age", "Income"]]
y_cls = df_classification["Purchased"]
x_train_cls, x_test_cls, y_train_cls, y_test_cls = train_test_split(x_cls, y_cls, test_size=0.2, random_state=42)

print(f"Training set: {x_train_cls.shape}")
print(f"Testing set: {x_test_cls.shape}")

print("Lojistik Regresyon Modeli Eğitiliyor...")
model_cls = LogisticRegression()
model_cls.fit(x_train_cls, y_train_cls)
print("Model eğitildi!")
print(f"Model katsayıları: {model_cls.coef_}")  

print("\n Lojistik Regresyon Modeli Tahmin Ediliyor...")
y_pred_cls = model_cls.predict(x_test_cls)
for gerçek, tahmin in zip(y_test_cls, y_pred_cls):
    print(f"Gerçek: {gerçek}, Tahmin: {tahmin}")

accuracy = accuracy_score(y_test_cls, y_pred_cls)
print(f"Doğruluk Skoru: {accuracy:.2f}")
print("\n Sınıflandırma Raporu:")
print(classification_report(y_test_cls, y_pred_cls))
print("\n Karmaşıklık Matrisi:")
print(confusion_matrix(y_test_cls, y_pred_cls))