# class -- anohter definition in python
# design
# class -- data and function
# attributes and methods
# def add(): x = 10
# object --- create an object for a class
# object will interact with its own class or with other class
# function(method) -- Behaviour

class class_room:
    def furnitures(self):
        print(f"The room is filled with furnitures")

grade5 = class_room()

print(type(grade5))

# __main__ - module name
# class_room -- class name
# <class '__main__.class_room'> -- our own class


grade6 = class_room()

class_room.furnitures()

class_room.furnitures(grade5)

class_room.furnitures(grade6)

grade5.furnitures()

grade6.furnitures()

# grade5 -- 10 tables and 5 chairs
# grade6 -- 5 tables and 3 chairs

# 'lenin'.upper() # 'LENIN'

# __init__ method -- special method in py
# __name__ -- special variable , *args , **kwargs

class class_room:
    def __init__(self):
        print(f"INside Init method")
    def furnitures(self):
        print(f"The room is filled with furnitures")

grade5 = class_room()

grade5.furnitures()

class class_room:
    def __init__(self, table, chair):
        self.table = table
        self.chair = chair
    def furnitures(self):
        print(f"The class room contains {self.table} Tables and {self.chair} Chairs")

grade5 = class_room('10', '5')
grade6 = class_room('5', '3')

grade5.furnitures()

grade6.furnitures()

#class:
#    def:

# Inheritance
# Polymorphism
# Encapsulation
# Abstracti0on

# class -- attributes and methods
# parent class
# child class -- will inhertit those attributes of the parent clas

class class_room:
    def __init__(self, name):
        self.name = name
    def students(self):
        print(f"The grade5 is handled by {self.name}")
class faculty(class_room):
    def __init__(self, name, sub_name):
        self.name = name
        self.sub_name = sub_name
    def subject(self):
        print(f" {self.name} teaches {self.sub_name}")

grade5 = faculty('Arun', 'Python')

grade5.students()

grade5.subject()

# class1 -- object1
# class2 -- object2
# class3 -- object3  -- parent class 

# types of polymorphism
# method overriding
# method overloading
# funtional polymorphism
# operator polymorphism

class shape:
    def area(self):
        pass
class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * 2

def area_calculation(shape):
    return shape.area()

rectangle = rectangle(2, 2)

circle = circle(2)

print(f"Area of rectangle : {area_calculation(rectangle)}")
print(f"Area of circle : {area_calculation(circle)}")
