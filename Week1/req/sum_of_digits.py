n=int(input("enter:"))
num=n
sum=0
while (n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
if(sum==num):
    print("sum of number of digits is equal to actual number")
else:
    print("the sum is not equal to actual number")