class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Teacher(Person):
    def __init__(self,name,age,teaching_sub):
        super().__init__(name,age)
        self.teaching_sub=teaching_sub
    def display(self):
        super().display()
        print("Teaching_sub:",self.teaching_sub)
class Student(Person):
    def __init__(self,name,age,standard):
        super().__init__(name,age)
        self.standard= standard
    def display(self):
        super().display()
        print("Standard:",self.standard)
s=Student("Nithya",21,"10th")
t=Teacher("Nithya",30,"Personality developement")
p=Person("Nithya",21)
lst=[s,t,p]
for each in lst:
    each.display()
