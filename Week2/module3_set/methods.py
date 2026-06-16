a={1,2,3,4,5,4,3,2,3}
print(a)

a.add(6)
print(a)

a.remove(5)
print(a)

# a.remove(0)
# print(a)

a.discard(0)
print(a)

p=a.pop()
print(p)
print(a)

a.clear()
print(a)

a={}
print(type(a))

a=set()
print(type(a))