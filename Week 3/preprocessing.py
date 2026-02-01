import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

def handle_missing_values(data):
    data["Gelir"] = data["Gelir"].fillna(data["Gelir"].mean())
    data["Cinsiyet"] = data["Cinsiyet"].fillna("Bilinmiyor")

    print("Eksik veriler işlendi.")
    print(data.isnull().sum())
    return data

def encode_categorical_data(data):

    label_encoder = LabelEncoder()
    data["Cinsiyet"] = label_encoder.fit_transform(data["Cinsiyet"])
    
    data = pd.get_dummies(data, columns=["Departman"], drop_first=True)

    print("Kategorik değişkenler kodlandı.")
    print(data.head())
    return data

def scale_data(data):
    scaler = StandardScaler()
    data[["Yaş", "Gelir", "Deneyim (Yıl)"]] = scaler.fit_transform(data[["Yaş", "Gelir", "Deneyim (Yıl)"]])
    print("Sayısal değişkenler ölçeklendi.")
    return data

def split_data(data):
    X = data.drop(["Terfi"], axis=1)
    y = data["Terfi"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("Veri seti eğitim ve test olarak ayrıldı.")
    return X_train, X_test, y_train, y_test
