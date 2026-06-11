# 1
# 21
# 321
# 4321
# 54321

n=int(input("enter:"))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j, end="")
    print()