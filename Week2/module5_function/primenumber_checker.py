# def prime(a):
#     count=0
#     for i in range(1,a+1):
#         count += a%i==0
#         # if (a%i==0):
#             # count+=1
#     return count

# n=int(input("enter num:"))
# prime(n)
# if(prime(n)==2):
#     print("Prime")
# else:
#     print("Not prime")

def prime(a):
    count=0
    for i in range(1,a+1):
        count += a%i==0
        if(count>2):
            return False
    if(count==2):
        return True

n=int(input("enter num:"))
p=prime(n)
if(p):
    print("Prime")
else:
    print("Not prime")

'''For any number n:

Check divisibility from 2 to √n (inclusive).
If no divisor is found, the number is prime.
eg:
math.isqrt(25) gives 5
then instead of checking 1 to 25 for prime check of a particular number 25
we can find sqrt and check for that one
for i in range(2,isqrt)'''

import math

def prime(a):
    if a < 2:
        return False

    for i in range(2, math.isqrt(a) + 1):
        if a % i == 0:
            return False

    return True


n = int(input("Enter number: "))

if prime(n):
    print("Prime")
else:
    print("Not Prime")