# above 80 marks

a=list(map(int,input("enter:").split()))
top=[]
for i in a:
    if(i>80):
        top.append(i)
print(sorted(top))

#remove duplicates

a=[10,20,20,30,20,10]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

#List comprehension
a=[10,20,30,20,40]
b=[i*2 for i in a]
print(b)