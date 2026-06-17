# # Square

# def sqr(a):
#     return (a*a)
# n=int(input("enter:"))
# print(sqr(n))

# # Cube

# def cube(a):
#     return (a*a*a)
# n=int(input("enter:"))
# print(cube(n))

# # Palindrome

# def is_palindrome(a):
#     rev=0
#     num=a
#     while(a>0):
#         rem=a%10
#         rev=(rev*10)+rem
#         a=a//10
#     if(a==rev):
#         return True
#     else:
#         return False
# n=int(input("enter :"))
# if (is_palindrome(n)):
#     print("Palindrome")
# else:
#     print("Not palindrome")

# Count vowels
def count_vowels(a):
    count=0
    vowels="aeiou"
    for i in a:
        if i.lower() in vowels:
            count+=1
    return count
n=input("enter:")
if(count_vowels(n)>0):
    print(count_vowels(n))
else:
    print("no vowels")