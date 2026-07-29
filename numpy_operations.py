import numpy as np

a = [1, 2, 3]

arr = np.array(a)

arr

a = (1, 2, 3)
arr1 = np.array(a)

arr1

arr = np.array([6, 7, np.nan, 9, 10])
arr

arr = arr[~np.isnan(arr)]

arr

mean = np.nanmean(arr)

mean

# x = 6, 7, nan, 9, 10  -- 1,000,000 - 20% -- 800,000
# y - independent varirable
# x - dependent variable
# x - attribute, column, features

arr = np.array([6, 7, np.nan, 9, 10])
arr

arr = np.nan_to_num(arr, nan = mean)
arr

# pandas - library - structured data

import pandas as pd

d = [1, 2, 3, 4, 5]
d

e = (1, 2, 3, 4, 5)
e

df = pd.Series(d)

df

df = pd.Series(e)

df

dic = {'a': 1, 'b': 2, 'c':3}
df = pd.Series(dic)
df

a = ['a', 'b', 'c']
b = [10, 20, 30]
df = pd.Series(b)
df 

df = pd.Series(b, index = a)

df

d = {'id': ['a', 'b', 'c'], 'mark': [100, 90, 80], 'name': ['Damien', 'stefan','Elena']}
df = pd.Series(d)
df

df = pd.DataFrame(d)
df

# when the data is very small to process - pandas

# decorators
# it takes another function as it input
# it adds an extra behaviour to existing function
# it returns new function

def addition(a, b):
    return a + b

addition(10, 20)

def my_decorator(func):
    print(f"Before add function")
    def add():
        print(f"Inside add method/function")
        func()
        print(f"After func call")
    return add
    print(f"End of decorator fucntion")

@my_decorator
def trigger_this():
    print(f"I am inside trigger method")

trigger_this()

def my_decorator(func):
    print(f"before add function")
    def add_num(*args, **kwargs):
        print(f"IPnside add method/fucntion")
        return func(*args, **kwargs)
        print(f"After func call")
    return add_num
    print(f"end of decorator")

@my_decorator
def trigger_this(p_return):
    print(f"{p_return}")

trigger_this("Trigger this method")

def first_function():
    print("Inside first fucntion")
    def second_function():
        print("INside second funtion")

second_function()

def add_num(*args):
    print(args, type(args))

add_num(1)

add_num('a')

add_num('a', 'b')

add_num('a', 'b', 'c', 'd')

def check_multiply(*args):
    result = 1
    for i in args:
        result *= i # result = result * i
    return result

print(check_multiply(2, 3, 4))

# kargs - keyword arguments, keys will be its argument name 
# * args - positional args
# **kwargs - keyword args

'''
tuple                  dict
Yes                     NO
Indexing method         specify the key pari '''

def define_kwargs(**kwargs):
    print(kwargs, type(kwargs))

define_kwargs(first_argument = 'Welcome', second_argument = 'Home')

def args_kwargs(*args, **kwargs):
    print(f"My args are {args}")
    print(f"My kwargs are {kwargs}")

args_kwargs(111, 222, first_argument = 'Welcome', second_argument = 'Home')

args_kwargs(11, 222)

def args_kwargs(*args, **kwargs):
    print(f"My args are {args}")
    print(f"My kargs are {kwargs}")
    print(args[0])
    print(kwargs['second_argument'])

args_kwargs(111, 222, 333, first_argument = 'Welcome', second_argument = 'Home')
