'''a= input("enter:")
b=a.split()
lst=[]
for i in b:
    if i not in lst:
        lst.append(i)
        print(i,b.count(i))'''

a=input("enter:").split()
new={}
count=0
for i in a:
    if( i in new):
        count+=1
        new[i]=count
    else:
        count=1
        new[i]=count
print(new)