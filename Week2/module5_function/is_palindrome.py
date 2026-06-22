# def is_palindrome(n):
#     rev=""
#     ori=n
#     for i in n:
#         if i.isspace():
#             continue
#         else:
#             rev=i.lower()+rev
#     return rev==ori
# n=input("enter:")
# if (is_palindrome(n)):
#     print("palindrome")
# else:
#     print("Not palindrome")

def is_palindrome(n):
    s=""
    rev=""
    for i in n:
        if(i==" "):
            continue
        else:
            s+=i
        rev=i+rev
    return s==rev
n=input("enter:")
if (is_palindrome(n)):
    print("Palindrome")
else:
    print("not palindrome")