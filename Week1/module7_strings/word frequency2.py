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