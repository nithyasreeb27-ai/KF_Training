import random

lst=[]
for i in range(10):
    a=random.randint(1,100)
    lst.append(a)
print(lst)
print(min(lst))
print(max(lst))
print(len(lst))
print(sum(lst))
print((sum(lst)/len(lst)))