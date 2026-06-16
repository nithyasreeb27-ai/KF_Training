d={
    101:{
        "name":"a",
        "dept":"IT",
        "salary":"700000"
    },
    102:{
        "name":"b",
        "dept":"HR",
        "salary":"600000"
    },
    103:{
        "name":"c",
        "dept":"IT",
        "salary":"750000"
    }
}

print("""Requirement:
    1. employee's details
    2. employee detail based on id
    3. employee detail based on name
      """)
n=int(input("enter your choice:"))
if(n==1):
    for key,value in d.items():
        print("roll:",key)
        print("name:",d[key]["name"])
        print("dept:",d[key]["dept"])
        print("salary:",d[key]["salary"])
    
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
else:
    print("invalid choice")