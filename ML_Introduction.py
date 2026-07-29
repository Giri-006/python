'''
ML:
1. Supervised learning
	1. REGRESSION
2. Unsupervised Learning

Y = F(X)

X = INDEPENDENT VARIABLE,
    COLUMN,
	FIELD,
	FEATURE,
	INPUT

Y = OUTPUT,
    DEPENDENT VARIABLE,
	PREDICTION
	
REGRESSION:
	1. Linear REGRESSION
	2. Logistic REGRESSION
	

Line equation:
y = f(x) = x2 + 1 = -3, -2, -1, 0 , 1, 2, 3
y = mx + c
y1 = mx1 + c

X = HOUR, SCORE, EDUCATIONAL_GRND

y = score --> f(x) --> x = hour
y = score --> f(x) --> x1 = hour, x2 = eductional_grnd
y = score --> f(x) --> x1 = hour, x2 = eductional_grnd, x3 = no_of_clas_attended
y = score --> f(x) --> x1 = hour, x2 = eductional_grnd, x3 = no_of_clas_attended, x4= students_previous_record

'''

import pandas as pd
import matplotlib.pyplot as plt

data = {'hours_studied': [1, 2, 3, 4, 5],
'score': [20, 30, 40, 50, 60]}


df = pd.DataFrame(data)

