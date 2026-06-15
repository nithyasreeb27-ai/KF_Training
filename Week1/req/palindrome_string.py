a=input("enter:")
rev=""
for i in a:
    rev=i+rev
if(a==rev):
    print("Palindrome")
else:
    print("Not palindrome")