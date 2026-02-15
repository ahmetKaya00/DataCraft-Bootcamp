import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score

df = pd.read_csv('bank.csv')
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

print(df['deposit'].value_counts())
print(df.isnull().sum())
print((df =='unknown').sum())

plt.hist(df['age'])
plt.title('Musteri Yas Dagilimi')
plt.xlabel('Yas')
plt.ylabel('Kisi Sayisi')
plt.show()

print(df.groupby('deposit')['age'].mean())
print(df.groupby('deposit')['balance'].mean())

plt.hist(df[df['deposit'] == 'yes']['balance'], alpha=0.5, label='Satın Alan')
plt.hist(df[df['deposit'] == 'no']['balance'], alpha=0.5, label='Satın Almayan')
plt.title('Bakiye Dagilimi')
plt.xlabel('Bakiye')
plt.ylabel('Kisi Sayisi')
plt.legend()
plt.show()

df = df.drop(['duration'], axis=1)
df_encoded = pd.get_dummies(df, drop_first=True)
print(df_encoded.shape)
X = df_encoded.drop('deposit_yes', axis=1)
y = df_encoded['deposit_yes']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

sclaler = StandardScaler()
X_train_scaled = sclaler.fit_transform(X_train)
X_test_scaled = sclaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

importance = pd.DataFrame({
    'Feature': X.columns, 
    'Importance': model.coef_[0]})
importance = importance.sort_values(by='Importance', ascending=False)
print(importance.head(10))

proba = model.predict_proba(X_test_scaled)
print("Predicted Probabilities:\n", proba[:10])

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

proba_yes = model.predict_proba(X_test_scaled)[:, 1]
threshold = 0.70
call_list = proba_yes >= threshold
print("Toplam test kisisi sayisi:", len(proba_yes))
print("Aranacak kisi sayisi:", call_list.sum())

top_n = 20
top_idx = proba_yes.argsort()[::-1][:top_n]
top_score = proba_yes[top_idx]
top_actual = y_test.iloc[top_idx].to_numpy()

for i, idx in enumerate(top_idx, start=1):
    score = proba_yes[idx]
    actual = y_test.iloc[idx]
    print(f"{i:02d} INDEX: {idx}, Skor: %{score*100:.1f}, Gercek Durum: {'Evet' if actual == 1 else 'Hayir'}")
