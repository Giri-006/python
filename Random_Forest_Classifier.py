from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = load_breast_cancer()

X = data.data
y = data.target

# a, b = 10, 20

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

'''
100 == 80 records training 20 records use it for test
'''

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


print("Accracy---", accuracy_score(y_test, y_pred))

print("\n******confusion_matrix***********")

print(confusion_matrix(y_test, y_pred)
)

print("\n*****classification report ********")

print(classification_report(y_test,y_pred))

'''
C:\Users\Admin\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_logistic.py:473: ConvergenceWarning: lbfgs failed to converge after 1000 iteration(s) (status=1):
STOP: TOTAL NO. OF ITERATIONS REACHED LIMIT

Increase the number of iterations to improve the convergence (max_iter=1000).
You might also want to scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
  n_iter_i = _check_optimize_result(
Accracy--- 0.956140350877193

******confusion_matrix***********
[[39  4]
 [ 1 70]]

*****classification report ********
              precision    recall  f1-score   support

           0       0.97      0.91      0.94        43
           1       0.95      0.99      0.97        71

    accuracy                           0.96       114
   macro avg       0.96      0.95      0.95       114
weighted avg       0.96      0.96      0.96       114
'''

import pandas as pd

data = pd.DataFrame({"Pregancies":[2, 5, 1, 6, 3, 8],
                     "glucose": [120, 150, 95, 180, 130, 170],
                     "BMI": [28, 35, 22, 40, 30, 38],
                     "age":[25, 45, 30, 50, 35, 55],
                     "Outcome": [0, 1, 0, 1, 0, 1]})
                
X = data[["Pregancies", "glucose","BMI", "age"]]
y  = data["Outcome"]

from skearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimator=3)

model.fit(X, y)

predict = model.predict([[5, 140, 30, 46]])

print(predict)
