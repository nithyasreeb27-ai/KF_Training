a=input("enter:")
new="" 
for i in a:
    if(i not in new):
        new+=i
        print(i,a.count(i))
