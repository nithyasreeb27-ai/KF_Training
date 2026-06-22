a= input("enter:")
b=a.split()
lst=[]
for i in b:
    if i not in lst:
        lst.append(i)
        print(i,b.count(i))

