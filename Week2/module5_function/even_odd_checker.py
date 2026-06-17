def is_even(a):
    return a%2==0
n=int(input("enter:"))
if is_even(n):
    print("Even")
else:
    print("Odd")


def even_odd(a):
    if(a%2==0):
        print(a,"is even")
    else:
        print(a,"is odd")
n=int(input("enter:"))
even_odd(n)