# Armstrong number

n=int(input("enter:"))
l=len(str(n))
num=n
a=0
for i in range(1,n+1):
    r=n%10
    a=r**l+a
    n=n//10
if(num==a):
    print("Armstrong number")
else:
    print("Not armstrong number")

