# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display_person(self):
#         print("Name:",self.name)
#         print(f"Age:{self.age}")
# class Employee(Person):
#     def __init__(self, name, age,emp_id,salary):
#         super().__init__(name, age)
#         self.emp_id=emp_id
#         self.salary=salary
#     def display_employee(self):
#         print(f"Name:{self.name}")
#         print(f"Age:{self.age}")
#         print(f"Emp_id:{self.emp_id}")
#         print(f"Salary:{self.salary}")
# class Manager(Employee):
#     def __init__(self, name, age, emp_id, salary,team_size):
#         super().__init__(name, age, emp_id, salary)
#         self.team_size=team_size
#     def display_manager(self):
#         print(f"Name:{self.name}")
#         print(f"Age:{self.age}")
#         print(f"Emp_id:{self.emp_id}")
#         print(f"Salary:{self.salary}")
#         print(f"Team size:{self.team_size}")
# new=Manager("Nithya",21,108,980000,6)
# new.display_person()
# new.display_employee()
# new.display_manager()
# # print(new.__dict__)



class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print(f"Age:{self.age}")
class Employee(Person):
    def __init__(self, name, age,emp_id,salary):
        super().__init__(name, age)
        self.emp_id=emp_id
        self.salary=salary
    def display(self):
        super().display()
        print(f"Emp_id:{self.emp_id}")
        print(f"Salary:{self.salary}")
class Manager(Employee):
    def __init__(self, name, age, emp_id, salary,team_size):
        super().__init__(name, age, emp_id, salary)
        self.team_size=team_size
    def display(self):
        super().display()
        print(f"Team size:{self.team_size}")
new=Manager("Nithya",21,108,980000,6)
# new.display_person()
# new.display_employee()
# new.display_manager()
new.display()