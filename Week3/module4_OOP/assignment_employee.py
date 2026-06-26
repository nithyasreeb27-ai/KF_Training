class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def display(self):
        print("ID:",self.id)
        print("Name:",self.name)
        print("Salary:",self.salary)
def get_input():
    print("id,name,salary")
    emp_id=int(input("enter id:"))
    name=input("enter name:")
    salary=float(input("enter salary"))
    return emp_id,name,salary

emp_id,name,salary=get_input()
s1=Employee(emp_id,name,salary)
s1.display()