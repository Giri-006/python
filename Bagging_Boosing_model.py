'''
1. LR
2. LOG R
3. Random Forest
 -- both LR AND LOG r
 -- N Number decision trees
 -- combined forma of all multiple decision tressd
 -- each tree will be trainer with different samples
 -- true/false
 
whether a patient having dibetes or not?
Tree1 -- 1
Tree2 -- 0
Tree3 -- 1
------------
final prediction -- majority votes
                 -- has dibetes

each tree
	random sample values -- for each
	radom columns/independent varaible
	
	
Ensemble learning method:

1. Bagging   -- model independt
2. Boosting  -- gradient boosing
3. Stacking

Predict diabetes:


1. age
2. blood count
3. insulin
4. bmi
5. bp
6. family history 
7. gender - male or female
8. diet
9. previous medication
   -- Pregnancy
   
'''


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.DataFrame({"Pregnancies":[2, 5, 1, 6, 3, 8],
"glucose": [120, 150, 95, 180, 130, 170],
"bmi": [28, 35, 22, 40, 30, 38],
"age": [25, 45, 30, 50, 35, 55],
"outcome": [0, 1, 0, 1, 1, 1]})

print(data)

X = data[["Pregnancies","glucose","bmi","age" ]]
y = data["outcome"]

model = RandomForestClassifier(n_estimators = 100)

# n of forest
# n < 50 unstable, high variance
# n = 100 to 300 
# n = 1000 -- waster of memory and cpy

model.fit(X, y)

predit_ = model.predict([[4, 140, 30, 41]])
print(f"my preicted value is {predit_}")


y_pred = model.predict(X)
print("Accuracy:", accuracy_score(y, y_pred))

'''
n_estimators = 3
D:\lenin\Practise_SF\B28>python ranforest.py
   Pregnancies  glucose  bmi  age  outcome
0            2      120   28   25        0
1            5      150   35   45        1
2            1       95   22   30        0
3            6      180   40   50        1
4            3      130   30   35        1
5            8      170   38   55        1
C:\Users\Admin\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\utils\validation.py:2749: UserWarning: X does not have valid feature names, but RandomForestClassifier was fitted with feature names
  warnings.warn(
my preicted value is [1]
Accuracy: 1.0


n_estimators = 100
D:\lenin\Practise_SF\B28>python ranforest.py
   Pregnancies  glucose  bmi  age  outcome
0            2      120   28   25        0
1            5      150   35   45        1
2            1       95   22   30        0
3            6      180   40   50        1
4            3      130   30   35        1
5            8      170   38   55        1
C:\Users\Admin\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\utils\validation.py:2749: UserWarning: X does not have valid feature names, but RandomForestClassifier was fitted with feature names
  warnings.warn(
my preicted value is [1]
Accuracy: 1.0
'''

#kaggle


'''
Baggging: -- 20000 rows
Step1: 
    Take 1000 rows -- sample 1000 rows with replacment -- 10 different sets of data
Step 2: 
    Train 10 different model --> each model sees differrent sets of dataq
Step 3:
    Regression : Average | Classification : Vote
'''


1. Baggine -- each of these 10 model will be trained independently 
           -- reduce the variance -- goal\
           -- overfiting -- lower
2. Boosing -- goal - to reduce the bias
           -- 1st modle will be trained first, 2nd model will be trained next -- sequences
           -- 2nd model -- error
           -- training the 3rd model -- get fixed and it will train the 3rd modle
           -- AdaBoost, XGBoost, LightGBM
           -- XGBoost  --- prediction
           -- As we increase the number of model to do the prediction the risk woudl be higher
