n=int(input("enter:"))
new=0
while(n>0):
    rem=n%10
    new=(new*10)+rem
    n=n//10
print(new)

