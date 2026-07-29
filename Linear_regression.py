import pandas as pd

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

data = {'Hours_studied': [1, 2, 3, 4, 5],
        'Score': [20, 30, 40, 50, 60]}
# dict  = {'a': [1, 2], 'b' : [10, 20]}

df = pd.DataFrame(data)

print("*****Student DataSet ******")
print(df)

X = df[['Hours_studied']]
print(X)
y = df['Score']
print(y)
model = LinearRegression()
model.fit(X,y)

print("\n*****Details of Model *****")
print("Slope :", model.coef_[0])
print("Intercept:",  model.intercept_)

print(f"\n**Regression Equation*****")
print(f"Score = {model.coef_[0]:.2f} * Hours_studied + {model.intercept_:.2f}")
# mx + b

hours = float(input("\nEnter number of hours studied:"))
predicted_score = model.predict([[hours]])
print(f"\nPredicted score for {hours} hours of study = {predicted_score[0]:.2f}")

df['predicted_score'] = model.predict(X)
print("\nDataset with predictions")
print(df)

plt.figure(figsize=(8, 5))
plt.scatter(df['Hours_studied'], df['Score'],
           color = 'blue', label='Actual Scores', s= 80)

plt.plot(df['Hours_studied'], model.predict(X), color='red', linewidth=3,label='Linear Regression Line')

plt.xlabel("Hours Studied")
plt.ylabel("Student Score")
plt.title("Linear Regression")
plt.legend()
plt.grid()



# language = {'english','tamil', 'english', 'english', 'english'}
# place_of_study = 

#{'english','tamil', 'english', 'english', 'english'}
# english - 1
# tamil - 2
