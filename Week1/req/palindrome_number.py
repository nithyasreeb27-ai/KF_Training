n=int(input("enter:"))
rev=0
num=n
while(n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
if(num==rev):
    print("Palindrome")
else:
    print("Not palindrome")