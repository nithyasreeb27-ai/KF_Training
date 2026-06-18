def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def is_even(a):
    return a%2==0
def is_prime(a):
    count=0
    for i in range(1,a+1):
        if (a%i==0):
            count+=1
    return count==2
def count_vowel(a):
    c=0
    vowel="aeiou"
    for i in a:
        if i.lower() in vowel:
            c+=1
    return c
def reverse(a):
    rev=""
    for i in a:
        rev=i+rev
    return rev

def menu(exp,*args):
    if(exp=="add"):
        return add(*args)
    elif(exp=="sub"):
        return sub(*args)
    elif(exp=="even"):
        return is_even(*args)
    elif(exp=="prime"):
        return is_prime(*args)
    elif(exp=="count_vowel"):
        return count_vowel(*args)
    elif(exp=="reverse string"):
        return reverse(*args)

print("""
Menu:
1.Mathematical
2.Checker
3.String operation""")

ch=int(input("enter your choice:"))
if(ch==1):
    print("""add
sub""")
elif(ch==2):
    print("""even
prime""")
elif(ch==3):
    print("""
count_vowel
reverse string""")
else:
    print("Invalid entry")

exp=input("enter expression number:")
if(exp=="add" or exp=="sub"):
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(menu(exp,a,b))
if(exp=="even" or exp=="prime"):
    a=int(input("enter:"))
    print(menu(exp,a))
if(exp=="count_vowel" or exp=="reverse string"):
    a=input("enter string:")
    print(menu(exp,a))