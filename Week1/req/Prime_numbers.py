# Prime numbers in range

n=int(input("enter:"))

for i in range(1,n+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if(count==2):
        print(i," is prime numbers")