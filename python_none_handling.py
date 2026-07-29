# 4. Use none in the condtional statement itself

value = None
if value is None:
    print(f"Block of code gets executed")

# 5. If None is present in the dictionary, how to validate it

user_profile = {'Name':'Siva','email': None}
#di = {'a': 10, 'b': None}
if user_profile['email'] is None:
    print(f"Block of code gets executed")

# assignment -- whichever value has none type, print those keys

user_profile = {'Name':'Siva','email': 'siva@gmail.com'}
#di = {'a': 10, 'b': None}
if user_profile['email'] is None:
    print(f"Block of code gets executed")
print(f"I am outside if statement")

# 6. Chaining of None

Name = None
if Name is not None:
    print(Name.isupper())
else:
    print(f"Name is not provided by the user")

Name = "Siva"
if Name is not None:
    print(Name.isupper())
else:
    print(f"Name is not provided by the user")

Name = "SIVA"
if Name is not None:
    print(Name.isupper())
else:
    print(f"Name is not provided by the user")

# lstrip -- removes the characters from teh lhs
# rstrip -- removes the characters from teh rhs
# strip --  removes the characters from boht the sides

string_ = "\nHelloWorld\n"
print(string_)
stripped_string = string_.strip()
print(stripped_string)

string_ = "    HelloWorld    "
print(string_)
stripped_string = string_.strip()
print(stripped_string)

string_ = "******Hello*****World*******"
print(string_)
stripped_string = string_.strip('*')
print(stripped_string)

string_ = "Hello*****World*******"
print(string_)
stripped_string = string_.rstrip('*')
print(stripped_string)

# Built-in functions
# string -- lower, upper, strip, join
# list -- append, remove, index, sort
# math -- abs, min, max, count, pow 
# len(), type(), print()

a = 10
b = 20
c = a + b

c

def add(x,y):
    c = x + y
    return c

add(10, 20)

add(11, 21)

def add():
    x, y = 10, 20
    c = x + y
    return c

add()

'raj'.upper()

def add(x, y):# argument, parameter, inputs
    #x, y = 10, 20
    c = x + y
    return c

add(10, 20)

def default_arg(name, message = "Hello"):
    print(f"{message} {name}")

default_arg('Siva')

default_arg('Siva','Welcome') # overide and overwrite

default_arg('Siva','Welcome','three')

def sum_num(*numbers):
    return sum(numbers) #  in-build match function

sum_num(5)

sum_num(5, 1)

sum_num(5, 1, 2)

sum_num([1, 2, 1]) # Assignment, U get the input in terms list only.
# Your python logic must extract the values from the list and use in the 
# above function

def square(numbers):
    return numbers ** 2

square(2)

square(5)

# factorial # applications that are used for
# factorial of 0 is 1 # assignment
# factorial of 1 is 1
# factorial of 2 is 2 * (2-1) = 2
# factorial of 3 is 3 * 2 * 1 = 6
# factorial of 4 is 4 * 3 * 2 * 1 = 24

def fact(numbers):
    if numbers == 0:
        return 1
    else:
        return numbers * fact(numbers - 1) # 3 * fact(3-1)
                                           # 3 * fact(2)
                                           # 3 * 2 * fact(1)
                                           # 3 * 2 * 1 * fact(0)
                                           # 3 * 2 * 1 * 1

fact(3)

def divide(a, b):
    c = a // b
    return c

divide(10, 2)

divide(10, 0) #ZeroDivisionError: integer division or modulo by zero

# modulo operation -- zero division error
