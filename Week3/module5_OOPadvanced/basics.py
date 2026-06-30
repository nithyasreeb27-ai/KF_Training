# class Student:

#     def __init__(self,name):
#         self.name=name

#     def display(self):
#         print(self.name)

# s=Student("John")


# # Level 1

# class Person:
#     def introduce(self):
#         print("Hi")
# class Employee(Person):
#     pass
# s=Employee()
# s.introduce()

# # Level 2

# class Animal:
#     def eat(self):
#         print("Ate")
# class dog(Animal):
#     pass
# class cat(Animal):
#     pass
# d=dog()
# d.eat()
# c=cat()
# c.eat()

# # Level 3

# class Vehicle:
#     def start(self):
#         print("started")
# class car(Vehicle):
#     def open_doors(self):
#         print("opened door")
# class bike(Vehicle):
#     def start(self):
#         print("Bike started")
# class bus(Vehicle):
#     def open_trunk(self):
#         print("Opened trunk")
# c=car()
# c.start()
# c.open_doors()
# b=bike()
# b.start()
# bu=bus()
# bu.open_trunk()
# bu.start()

# # Constructor init

# class Person:
#     def __init__(self):
#         print("Hello")
# class Student(Person):
#     def new(self):
#         print("New")
# s=Student()
# s.new()

# # Mulitiple inheritance 

# class A:
#     def skills(self):
#         print("A")
# class B:
#     def skills(self):
#         print("B")
# class C(A,B):
#     pass
# c=C()
# c.skills()
# print(C.mro())

# # Diamond

# class A:
#     def hello(self):
#         print("A")
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B, C):
#     pass
# d=D()
# d.hello()
# print(D.mro())


class Person:
    def __init__(self):
        self.name = "John"


class Employee(Person):
    def __init__(self):
        self.salary = 50000


e = Employee()

print(e.salary)
print(e.name)