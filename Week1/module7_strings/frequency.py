a=input("enter:")
new={}
for i in a:
    if(i in new):
        new[i]+=1
    else:
        new[i]=1
print(new)