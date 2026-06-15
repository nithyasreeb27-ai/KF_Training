# store student detail as tuple and access it

tpl=(1,"a",98)
print(tpl[1])
print(tpl.count("a"))
print(tpl.index(98))

#Store student details as tuple in list

n=int(input("enter number of students:"))
lst=[]
for i in range(n):
    name=input("enter name:")
    subject=input("enter subject:")
    mark=int(input("enter mark:"))
    t= name, subject, mark
    lst.append(t)
print(tuple(lst))