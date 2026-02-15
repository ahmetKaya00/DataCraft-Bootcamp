from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay,confusion_matrix
import matplotlib.pyplot as plt

iris = load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(f"Training set: {x_train.shape}")
print(f"Testing set: {x_test.shape}")

print("Karar Ağacı Modeli Eğitiliyor...")
model_dt = DecisionTreeClassifier()
model_dt.fit(x_train, y_train)
print("Model eğitildi!")
print("\n Karar Ağacı Modeli Tahmin Ediliyor...")
y_pred_dt = model_dt.predict(x_test)
print(f"Doğruluk Skoru: {accuracy_score(y_test, y_pred_dt):.2f}")

print("\n Random Forest Modeli Eğitiliyor...")
model_rf = RandomForestClassifier(n_estimators=100, random_state=42)
model_rf.fit(x_train, y_train)  
y_pred_rf = model_rf.predict(x_test)
print("Model eğitildi!")
print(f"Doğruluk Skoru: {accuracy_score(y_test, y_pred_rf):.2f}")

new_flower = [[5.1, 3.5, 1.6, 4.5]]
predicted_class_dt = model_dt.predict(new_flower)
predicted_class_rf = model_rf.predict(new_flower)
print(f"Karar Ağacı Tahmini: {iris.target_names[predicted_class_dt][0]}")
print(f"Random Forest Tahmini: {iris.target_names[predicted_class_rf][0]}")
x_petal = x[:, [2,3]]

for label, color, species in zip((0,1,2), ['red', 'green', 'blue'], iris.target_names[0]):
    plt.scatter(x_petal[y==label, 0],
                x_petal[y==label, 1], c=color, label=species)
plt.xlabel('Petal Length')
plt.ylabel('Species')
plt.title('Iris Dataset - Petal Length vs Species') 
plt.legend()
plt.grid()
plt.show()


cm = confusion_matrix(y_test, y_pred_dt)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot(cmap=plt.cm.Blues)
plt.title('Random Forest Confusion Matrix')
plt.show()
