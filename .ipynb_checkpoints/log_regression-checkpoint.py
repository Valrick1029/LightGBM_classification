import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


df = pd.read_parquet("dataset.parquet")
df = df.drop('wallet_address', axis=1)


X = df[df.columns[:-1]]
y = df['target']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LogisticRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print(f"Точность модели логарифмической регрессии: {accuracy * 100:.2f}%")


print("Матрица ошибок:")
print(confusion_matrix(y_test, y_pred))


print("Отчет о классификации:")
print(classification_report(y_test, y_pred))

