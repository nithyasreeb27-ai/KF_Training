# *****
#  ****
#   ***
#    **
#     *

n=int(input("enter:"))
for i in range(n,0,-1):
    for space in range(n-i):
        print(" ",end="")
    for star in range(i):
        print("*",end="")
    print()