# list values along with index

# l=[10,20,30,40]
# for i in l:
#     print(f"index{l.index(i)} ->{i}")

#elements in reverse order

l=[10,20,30,40]
for i in range(len(l)-1,-1,-1):
    print(l[i])

l=[10,20,30,40]
for i in l[::-1]:
    print(i)