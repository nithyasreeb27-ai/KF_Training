age=int(input("enter age:"))
citizen=input("enter citizen:")
if(age>=18 and citizen=="indian"):
    print("Eligible")
elif(age<0):
    print("Invalid")
else:
    print("Not eligible")