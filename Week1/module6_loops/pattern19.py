#     1
#    222
#   33333
#  4444444
# 555555555

n=int(input("enter:"))
for i in range(1, n+1):
    for space in range(n-i):
        print(" ",end="")
    for num in range(2*i-1):
        print(i, end="")
    print()