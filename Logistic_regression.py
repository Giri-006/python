from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = load_breast_cancer()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state= 42)

'''
100 --- 80 records (training)
'''

model = LogisticRegression(max_iter= 1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy-------", accuracy_score(y_test, y_pred))

print("\n**************Confusion Matrix***************")

print(confusion_matrix(y_test, y_pred))

print("\n*********Classification report************")

print(classification_report(y_test, y_pred))
