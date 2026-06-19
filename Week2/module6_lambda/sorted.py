# new list

a=[1,4,2,4,6,7,5,3]
b=sorted(a)
print(a)
print(b)

# sorted with normal and  key len

a=["ai","nithyasree","python"]
print(sorted(a))
b=sorted(a,key=len)
print(b)

# sorted based on name and marks

a=[
 ('Abi',70),
 ('John',95),
 ('Ram',80)
]
print(sorted(a))
b=sorted(
    a,
    key=lambda x:x[0]
)
print(b)
c=sorted(
    a,
    key=lambda x:x[1],
    reverse=True
)
print(c)