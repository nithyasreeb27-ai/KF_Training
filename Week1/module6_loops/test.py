# ****
# *
# ****
# *
# ****

n=int(input("enter:"))
for i in range(1, n+1):
    for j in range(1,n+1):
        if(j==1 or i%2!=0):
            print("*",end="")
    print()