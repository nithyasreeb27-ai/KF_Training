#Employee Record viewer
print("*************************")
print("Employee Record Viewer")
print("*************************")
tpl=[(1,"a","IT",400000),
     (2,"b","HR",500000),
     (3,"c","Finance",350000),
     (4,"d","IT",7000000)]
print("""
      1.view one employee record using id
      2.view one employee record using name
      3.view employee details per department
      4.view count per department
      5.view highest salary employee detail
      6.view lowest salary employee details
      7.view all employee records  
      """)
a=int(input("enter your choice:"))
if(a==1):
     emp_id=int(input("enter employee id to view their record:"))
     for employee in tpl:
          id,name,dept,salary=employee
          if emp_id==id:
               print(f"""
     ID     :{id} 
     name   :{name}
     dept   :{dept} 
     Salary :{salary}
               """)
               break
     else:
          print("employee id not found")
elif(a==2):
     emp_name=input("enter employee name to view their record:")
     for employee in tpl:
          id,name,dept,salary=employee
          if emp_name==name:
               print(f"""
     ID     :{id} 
     name   :{name}
     dept   :{dept} 
     Salary :{salary}
               """)
               break
     else:
          print("employee name not found")

elif(a==3):
     n=input("enter dept:")
     for employee in tpl:  
          id,name,dept,salary=employee
          if(dept==n):
               print(employee,end="\n")

elif(a==4):
     n=input("enter dept:")
     count=0
     for employee in tpl:  
          id,name,dept,salary=employee
          if(n==dept):
               count+=1
     print("count:",count)

elif(a==5):
     highest_salary=float("-inf")
     for employee in tpl:
          id,name,dept,salary=employee
          if(salary> highest_salary):
               highest_salary=salary
          print("Highest salary:",highest_salary)

elif(a==6):
     lowest_salary = min(employee[3] for employee in tpl)
     print("Lowest salary:", lowest_salary)
          
elif(a==7):
     for employee in tpl:
          id,name,dept,salary=employee
          print(f"""
     ID     :{id} 
     name   :{name}
     dept   :{dept} 
     Salary :{salary}
               """)
          #print(employee,end="\n")

else:
     print("Invalid choice")