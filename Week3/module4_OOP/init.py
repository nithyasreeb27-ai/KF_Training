# General

'''class student:

    def __init__(self):
        print("Student object created")

s1=student()
s2=student()'''

# variable in init(self)

'''class Student:
    def __init__(self):
        self.name="Nithya"
s1=Student()
print(s1.name)'''

# constructor with parameters

'''class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("Nithyasree",21)
print(s1.name,s1.age,s1)'''

# Method

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
s=student("a",100)
s.display()
student.display(s)


# # Modification using methods

# class Bankaccount:
#     def __init__(self,name,amount):
#         self.name=name
#         self.balance=amount
#     def display(self,amount):
#         self.balance=self.balance+amount
# a=Bankaccount("a",1000)
# print(a.balance)
# a.display(100)
# print(a.balance)