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