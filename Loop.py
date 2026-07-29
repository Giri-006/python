#1
#2
#3

# for loop conditioonal statements
# my program to execute in sequences
# sequences - iterator (int, str, list, tuple, dict)
# 1 to 5

for i in 5: #TypeError: 'int' object is not iterable
    print(i)

for i in range(5):# 0.1.2.3.4
    print(i)

for i in range(5):# 0.1.2.3.4
    print(i)
print('No more vales present inside the for loop')

for i in range(5):# 0.1.2.3.4
    print(f"Before if statement {i}")
    if i == 3:
        print(i)
        break
    print('I am  outside if statement')
print('No more vales present inside the for loop')

for i in range(5):# 0.1.2.3.4
    print(f"Before if statement {i}")
    if i == 3:
        print(i)
        continue
    print('I am  outside if statement')
print('No more vales present inside the for loop')

#start_pos:end_pos:no_of_steps
#end_pos = end_pos - 1
# no_of_steps = no_of_steps - 1

for i in range(1, 5):
    print(f"I am inside for condition, {i}")
print(f"outside for loop")

#1 2 3 4 5 6 7 8 9 
for i in range(1, 10, 2):
    print(f"I am inside for condition, {i}")
print(f"outside for loop")

for i in range(1, 10, 3):
    print(f"I am inside for condition, {i}")
print(f"outside for loop")

for i in range(-10, 10, 3):
    print(f"I am inside for condition, {i}")
print(f"outside for loop")

for i in range(-10, -15, 3):
    print(f"I am inside for condition, {i}")
print(f"outside for loop")

print('S')
print('I')
print('V')
print('A')

for i in 'SIVA':
    print(f"{i}")

name = 'SIVA'
j = 0
for i in name:
    j = j + 1 
    # j = 1
    # j = 2 --> j = j + 1
    # j = 3 --> j = j + 1
    print(f"{i}  -- {j}")

name = 'sIVa'
j = 0
for i in name:
    if i.isupper():
        j = j + 1
print(f"value of j is {j}")

name = 'sIVa'
for i, j in enumerate(name):
    print(f"{i} -- {j}")

li = ['employee_id','first_name','last_name']
for i, j in enumerate(li):
    print(f"{i} -- {j}")

tu = ('employee_id','first_name','last_name')
for i, j in enumerate(tu):
    print(f"{i} -- {j}")

di = {'100':'employee_id','101':'first_name','102':'last_name'}
for i, j in enumerate(di):
    print(f"{i} -- {j}")

di = {'100':'employee_id','101':'first_name','102':'last_name'}
for i, j in enumerate(di, 1):
    print(f"{i} -- {j}")

di = {'100':'employee_id','101':'first_name','102':'last_name'}
for i, j in enumerate(di, 11):
    print(f"{i} -- {j}")

li = [['a', 'b '], ['c', 'd'], ['e','f']]
for i in li:
    print(i)

li = [['a', 'b '], ['c', 'd'], ['e','f']]
for i in li:
    for j in i:# ['a', 'b']
        print(j, end = " ")
    print()
    print("Outside loop j")
print("outside loop i")
