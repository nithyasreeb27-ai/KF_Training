#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

n=int(input("enter:"))
for i in range(1,n+1):
    for space in range(n-i):
        print(" ", end="")
    for inc in range(1,i+1):
        print(chr(64+inc), end="")
    for dec in range(1,i):
        print(chr(64+i-dec), end="")
    print()