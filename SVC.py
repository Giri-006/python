'''
SVM:

Types:

1. SVC -- support vector classification
2. SVR -- support vecor regression
3. OneClassSVM


* when our dataset is clean --kernel = 'linear' 
* when our dataset is complex -- kernel = 'rbf' -- curved linear
* C = 1.0
* gamma = how much 1 point influence?


dataset = 50,000 -- dataset is not likely to grow -- RF
dataset = < 50,000 -- dataset is likely to grow -- SVM
Training = 

confusion matrix 

			Predicted Yes Predicted No
Actual Yes     TP             FN
Actual NO      FP             TN


Precision =  TP / (TP + FP)
Recall =  TP / (TP + FN) -- dectection, how many real patients we saved
F1 Score = Balance precision and recall

'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = pd.DataFrame({
"glucose":[85, 89, 90,  95, 100, 115, 110, 115, 120, 125, 130, 140, 145, 150, 155, 160,165, 170, 180],
"bmi":[21, 22, 23, 24, 25, 26, 27, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38],
"outcome":[0,0,0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1]
})

X = data[["glucose", "bmi"]]
y = data["outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

model = SVC(kernel = "linear")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("classification_report:", classification_report(y_test, y_pred))
print("confusion_matrix:", confusion_matrix(y_test, y_pred))
print("confusion_matrix:", confusion_matrix(y_test, y_pred))

'''
plt.figure(figsize= (10,6))

for lable, color, name in zip([0,1],["blue","red"], ["non-diabetic", "diabetic"]):
    subset = data[data["outcome" == label]]
    plt.scatter(subset["glucose"],
                subset["bmi"],
                label=name,
                edgecolors = "k",
                s= 100)
'''
