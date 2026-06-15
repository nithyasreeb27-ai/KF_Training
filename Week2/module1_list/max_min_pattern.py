# largest element

l=[10,20,40,30]
b=sorted(l)
print(max(b))

a=[1,2,4,8]
largest=a[0]
for i in range(1,len(a)):
    if(a[i]>largest):
        largest=a[i]
print(largest)

# Smallest
a=[10,20,15,24]
smallest=a[0]
for i in a:
    if(i<smallest):
        smallest=i
print(smallest)

#Second Largest element
a=[10,20,30,40,33,27]
largest=float('-inf')
second=float('-inf')
for i in a:
    if(i>largest):
        second=largest
        largest=i
    elif(i>second):
        second=i
print("largest",largest)
print("Second largest",second)

#nested loop

a=[
    [1,2],
    [3,4]
]
sum=0
for i in a:
    for j in i:
        sum+=j
print(sum)

#nested loop maximun
a=[
    [10,20],
    [60,40]
]
largest=float("-inf")
for i in a:
    for j in i:
        if j>largest:
            largest=j
print(largest)