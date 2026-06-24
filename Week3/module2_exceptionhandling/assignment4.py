# Pattern1

class neg(Exception):
    pass
try:
    age=int(input("enter age:"))
    if(age<0):
        raise neg("Age should be positive")
    salary=float(input("enter salary:"))
    if(salary<0):
        raise neg("salary should be positive")
except ValueError:
    print("Enter the correct value.")
except neg as i:
    print(i)

# Pattern2

try:
    age=int(input("enter age:"))
    if(age<0):
        raise ValueError("Age should be positive")
    salary=float(input("enter salary:"))
    if(salary<0):
        raise ValueError("salary should be positive")
except ValueError as v:
    print(v)