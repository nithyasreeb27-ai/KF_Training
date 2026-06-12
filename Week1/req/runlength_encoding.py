a=input("enter:")
previous=a[0]
count=1
s=""

for i in range(1,len(a)):
    if(previous==a[i]):
        count+=1
    else:
        s+=previous+str(count)
        previous=a[i]
        count=1
s+=previous+str(count)
print(s)