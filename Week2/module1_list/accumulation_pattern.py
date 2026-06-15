#count,total,sum,average

#sum-1
a=[1,2,3,4]
sum=0
for i in a:
    sum+=i
print(sum)

#sum-2
# a=[1,2,3,4]
# print(sum(a))

#product

a=[1,2,3,4]
product=1
for i in a:
    product*=i
print(product)

#Average

a=[1,2,3]
total=0
l=len(a)
for i in a:
    total+=i
avg=total/l
print(avg)