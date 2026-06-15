# check a number exists

l=[1,2,3,4]
if 2 in l:
    print("exist")

#index of first occurence

a=[10,20,30,20]
for i in a:
    if(i==20):
        print(a.index(i))
        break

#Counting of even numbers

a=[1,2,3,4,2,3,1]
count=0
for i in a:
    if(i%2==0):
        count+=1
print(count)    

# count positive numbers

a=[1,2,3,4,2,0,-3,-1,4]
count=0
for i in a:
    if(i>0):
        count+=1
print(count)    