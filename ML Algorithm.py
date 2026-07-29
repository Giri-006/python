'''
Logistic Regression -- Supervised learning

Linear Regression -- continous data 

Logistic Regression -- Supervised learning

-- classification algorithm


Studied_hours

1                       No
2                       No
3                       Yes
4                       Yes
5                       Yes

studied_hours = 1, 2(No)
              = 3, 4, 5 (Yes)
			  
why can't we use linear regression:

probaility = 1.4 , -0.3

0 and 1

sigmoid function

other s-shaped curve

I would set the boundary, that i will call threshold

any probailities that is > 0.5 i woudl says that it has success case else failure case

threshold = 0.5

Types of logistic REgression:
\
1. binary LR
2. multinomail LR
3. ordinal LR  -- Feed back OLR

'''


import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {'studied_hours':[1,2,3,4,5,6],
        'pass':[0,0,0,1,1,1]}

df = pd.DataFrame(data)

#y = output/dependent variable
#X = input/independent varible
X =  df[['studied_hours']]
y =  df[['pass']]

model = LogisticRegression()
model.fit(X, y)

prediction =  model.predict([[7]])
probability = model.predict_proba([[7]])

print("Prediction:", prediction)
print("probability:", probability)


'''
Expected output:
    
Prediction: [1]
probability: [[0.01940625 0.98059375]]


'''
