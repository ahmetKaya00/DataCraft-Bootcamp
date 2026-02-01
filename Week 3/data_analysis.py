import pandas as pd

data = pd.DataFrame({
    "Yaş": [25, 45, 30, 35, 40],
    "Cinsiyet": ["Erkek", "Kadın", "Kadın", "Erkek", None],
    "Gelir": [3000, 7000, None, 5000, 6000],
    "Deneyim (Yıl)": [2, 20, 5, 10, 15],
    "Departman": ["IT", "Yönetim", "Muhasebe", "IT", "Yönetim"],
    "Terfi": [0, 1, 0, 1, 1]
})

print("Veri setinin ilk 5 satırı:")
print(data.head())

print("\nVeri setinin özet bilgisi:")
print(data.info())

print("\nEksik verilerin sayısı:")
print(data.isnull().sum())

print("\nTemel istatistiksel özet:")
print(data.describe())