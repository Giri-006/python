import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
data = pd.DataFrame({"Pregancies":[2, 5, 1, 6, 3, 8],
                     "glucose": [120, 150, 95, 180, 130, 170],
                     "BMI": [28, 35, 22, 40, 30, 38],
                     "age":[25, 45, 30, 50, 35, 55],
                     "Outcome": [0, 1, 0, 1, 0, 1]})
                     
                
X = data[["Pregancies", "glucose","BMI", "age" ]]
y  = data["Outcome"]


model = RandomForestClassifier(n_estimators=3)

model.fit(X, y)

predict = model.predict([[5, 140, 30, 46]])

print(predict)

y_pred = model.predict(X)

print("***Accuracy***:", accuracy_score(y, y_pred))

