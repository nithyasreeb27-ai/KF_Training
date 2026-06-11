#     1
#    22
#   333
#  4444
# 55555

n=int(input("enter:"))
for i in range(1,n+1):
    for space in range(n-i):
        print(" ", end="")
    for num in range(i):
        print(i, end="")
    print()