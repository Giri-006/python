names = ['Giri','Harshini','Chris']
Ages = [20, 21, 22]
for na, ag in zip(names, Ages):
    print(f"{na} is {ag} years old.")

person_li = [('Giri', 20), ('Harishini',21), ('Chris',22)]
names, age = zip(*person_li)
print(names)
print(age)

person_li = [['Giri', 20], ['Harishini',21], ['Chris',22]]
names, age = zip(*person_li)
print(names)
print(age)

num_ = [1, 2, 3, 4, 5]
sq_num = num_ ** 2
print(sq_num)

num_ = [1, 2, 3, 4, 5]
sq_num = [i ** 2 for i in num_]
#[i ** 2 
# for i in num_]
print(sq_num)

num_ = [1, 2, 3, 4, 5]
sq_even_num = [i ** 2 for i in num_ if i%2 == 0]
print(sq_even_num)

num_ = [1, 2, 3, 4, 5]
sq_even_num = [i for i in num_ if i%2 == 0]
print(sq_even_num)

num = [3, 1, 5, 4, 2]
max_num = num[0]# 3, 5
for i in num:
    if i > max_num:
        max_num = i
print(max_num)

# while

count = 0
while count < 5:
    print(count)
    count += 1 # count = count + 1
# how you 'can make this while loop to run infinittely and how to break
# looping 

# sh command
# command2

while True:
    print("This loop runs forever! Before Break!")
    pass
    print("This loop runs forever! After Pass!")
    break
    print(f"After break")
print("OUtside loop")

user_input = ""
while user_input != "exit":
    # executable logic
    user_input = input("Type 'exit' to Stop:")
    print("Typed input", user_input)

x = None # it's a special value and represents the absence of value or null value
print(x, type(x))

#1. when the function get assigned to a variable it returns none type

#function

def welcome():
    print(f"Welcome to Aimore Technologies")

welcome()

def welcome():
    return f"Welcome to Aimore Technologies"

welcome()

def get_user_input():
    user_input = ""
    while user_input != "exit":
        user_input = input("Type 'exit' to Stop:")
        print("Typed input", user_input)

get_user_input()

result = welcome()

result

print(result, type(result))

def welcome():
    print(f"Welcome to Aimore Technologies")

result = welcome()
print(result, type(result))

# 2. direct assignment of none to variable

# 3. Functions return None when teh  condition does not match

def get_even_number(numbers):
    for i in numbers:
        if i % 2 == 0:
            return i
    return None

get_even_number(3)

get_even_number([1, 3, 4, 2])

result = get_even_number([1, 3, 4, 2])
print(result)

result = get_even_number([1, 3, 5, 7])
print(result)
