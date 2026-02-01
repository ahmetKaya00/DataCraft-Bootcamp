from preprocessing import handle_missing_values, encode_categorical_data, scale_data, split_data
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

if __name__ == "__main__":
    # Veri setini oluşturma
    data = pd.DataFrame({
        "Yaş": [25, 45, 30, 35, 40],
        "Cinsiyet": ["Erkek", "Kadın", "Kadın", "Erkek", None],
        "Gelir": [3000, 7000, None, 5000, 6000],
        "Deneyim (Yıl)": [2, 20, 5, 10, 15],
        "Departman": ["IT", "Yönetim", "Muhasebe", "IT", "Yönetim"],
        "Terfi": [0, 1, 0, 1, 1]
    })

    print("Orijinal Veri Seti:")
    print(data)

data = handle_missing_values(data)
data = encode_categorical_data(data)

scaler = StandardScaler()
data[["Yaş", "Gelir", "Deneyim (Yıl)"]] = scaler.fit_transform(data[["Yaş", "Gelir", "Deneyim (Yıl)"]])

x = data.drop("Terfi", axis=1)
y = data["Terfi"]
X_train, X_test, y_train, y_test = split_data(data)


model = LogisticRegression()
model.fit(X_train, y_train)

new_eployee = pd.DataFrame({
    "Yaş": [40],    
    "Cinsiyet": [2],
    "Gelir": [4500],
    "Deneyim (Yıl)": [6],
    "Departman_Muhasebe": [1],
    "Departman_Yönetim": [0]
})

new_eployee[["Yaş", "Gelir", "Deneyim (Yıl)"]] = scaler.transform(new_eployee[["Yaş", "Gelir", "Deneyim (Yıl)"]])

prediction = model.predict(new_eployee)

if prediction[0] == 1:
    print("Yeni çalışan terfi alacaktır.")
else:
    print("Yeni çalışan terfi almayacaktır.")