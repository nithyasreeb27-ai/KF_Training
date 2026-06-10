#Same thig every row

'''n=int(input("enter:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*", end="")
    print()'''

#increasing pattern

'''n=int(input("enter:"))
for row in range(1,n+1):
    for col in range(row):
        print("*",end="")
    print()'''

#decreasing pattern

'''n=int(input("enter:"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()'''

#number pattern increasing

'''n=int(input("enter:"))
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end="")
    print()'''

#number pattern decreasing

'''n=int(input("enter:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()'''

#Repeated increasing number

'''n=int(input("enter:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()'''

# Reverse repeated decreasing pattern

"""n=int(input())
num=n
for i in range(n):
    num=n-i
    for j in range(n-i):
        print(num, end="")
    print()"""

#Alphabet increasing

'''n=int(input("enter:"))
for i in range(1, n+1):
    for j in range(i):
        print(chr(65+j),end="")
    print()'''

#Reverse Alphabet pattern

'''n=int(input("enter:"))
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j),end="")
    print()'''

#Right aligned pattern(1)

'''n=int(input("enter:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i+j<=5):
            print(" ",end="")
        else:
            print("*",end="")
    print()'''

#Right aligned pattern(2)

'''n=int(input("enter:"))
for i in range(1, n+1):
    for space in range(n-i):
        print(" ",end="")
    for star in range(i):
        print("*",end="")
    print()'''


#pyramid pattern(1)

'''n=int(input("enter:"))
for i in range(1, n+1):
    for space in range(n-i):
        print(" ",end="")
    for star in range(2*i-1):
        print("*",end="")
    print()'''

#pyramid pattern(2)

'''n=int(input("enter:"))
for i in range(1,n+1):
    for j in range(1,2*n):
        if(j>=n-i+1 and j<=n+i-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()'''

#Inverted pyramid

'''n=int(input("enter:"))
for i in range(n,0,-1):
    for space in range(n-i):
        print(" ",end="")
    for star in range(2*i-1):
        print("*",end="")
    print()'''

# Diamond pyramid

'''n=int(input("enter:"))
for i in range(1, n+1):
    for space in range(n-i):
        print(" ",end="")
    for star in range(2*i-1):
        print("*",end="")
    print()
for j in range(n,0,-1):
    for space in range(n-j):
        print(" ",end="")
    for star in range(2*j-1):
        print("*",end="")
    print()'''

# Increasing numberwise / Floyd's triangle

'''n=int(input("enter:"))
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num, end=" ")
        num+=1
    print()'''

# reverse number pattern

'''1
21
321
4321
54321

n=int(input("enter:"))
for i in range(1,n+1):
    for j in range(i):
        print(i-j, end="")
    print()'''

# Hollow square

n=int(input("enter:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or i==5 or j==1 or j==5):
            print("*",end="")
        else:
            print(" ",end="")
    print()