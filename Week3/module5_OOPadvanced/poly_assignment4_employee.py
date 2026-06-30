class Employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
    def display(self):
        print(self.name)
        print(self.emp_id)

class Fulltime(Employee):
    def __init__(self,name,emp_id,salary):
        super().__init__(name,emp_id)
        self.salary=salary
    def display(self):
        super().display()
        print(self.salary)

class Parttime(Employee):
    def __init__(self,name,emp_id,hours,rate):
        super().__init__(name,emp_id)
        self.hours=hours
        self.rate=rate
    def display(self):
        super().display()
        print(self.hours*self.rate)

class Freelancer(Employee):
    def __init__(self,name,emp_id,project,payment):
        super().__init__(name,emp_id)
        self.project=project
        self.payment=payment
    def display(self):
        super().display()
        print(self.project*self.payment)

ft=Fulltime("Nithya",174,750000)
pt=Parttime("abc",111,7,200)
fl=Freelancer("xyz",99,7,16000)
employees=[ft,pt,fl]
for employee in employees:
    employee.display()