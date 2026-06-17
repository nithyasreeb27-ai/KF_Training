d={
    101:{
        "name":"a",
        "dept":"IT",
        "salary":700000
    },
    102:{
        "name":"b",
        "dept":"HR",
        "salary":600000
    },
    103:{
        "name":"c",
        "dept":"IT",
        "salary":750000
    }
}

print("""Requirement:
    1. employee's details
    2. employee detail based on id
    3. employee detail based on name
    4. employee who get highest salary
    5. employee who get lowest salary
      """)
n=int(input("enter your choice:"))
if(n==1):
    for key,value in d.items():
        print("roll:",key)
        print("name:",d[key]["name"])
        print("dept:",d[key]["dept"])
        print("salary:",d[key]["salary"],"\n")
    
elif(n==2):
    emp_id=int(input("enter:"))
    if emp_id in d.keys():
        print(d[emp_id])
    else:
        print("invalid entry")

elif(n==3):
    emp_name=input("enter:")
    for key,value in d.items():
        if (value["name"]==emp_name):
            print(d[key])
            break
    else:
        print("invalid entry")
elif(n==4):
    sal=[]
    emp=[]
    for key,value in d.items():
        for key1,value1 in value.items():
            if key1=="salary":
                sal.append(value1)
                emp.append(value["name"])
    for i in sal:
        if(i==max(sal)):
            print("Highest Salary employee is:",emp[sal.index(i)])
            print("Highest Salary is:",(max(sal)))
                  
elif(n==5):
    lowest_salary=float("inf")
    low_salary_employee=""
    for key,value in d.items():
        if(value["salary"]<lowest_salary):
            lowest_salary=value["salary"]
            low_salary_employee=value["name"]
    print("Lowest salary:",lowest_salary)
    print("Employee with lowest salary",low_salary_employee)

else:
    print("invalid choice")