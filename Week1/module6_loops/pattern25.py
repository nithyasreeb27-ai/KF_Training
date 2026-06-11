#     1
#    121
#   12321
#  1234321
# 123454321

n=int(input("enter:"))
for i in range(1,n+1):
    for space in range(n-i):
        print(" ", end="")
    for inc in range(1,i+1):
        print(inc, end="")
    for dec in range(i-1,0,-1):
        print(dec, end="")
    print()
