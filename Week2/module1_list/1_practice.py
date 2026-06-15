#collection of marks

n=int(input("enter number of students:"))
marks=[]
for i in range(n):
    mark=int(input("enter mark:"))
    marks.append(mark)
print(marks)

#Highest and Lowest mark

print("highest",max(marks))

smallest=float("inf")
for small in marks:
    if (small<smallest):
        smallest=small
print("smallest",smallest)

#Remove duplicates

a=[10,20,20,30,10]
d=[]
for i in a:
    if i not in d:
        d.append(i)
print("removed duplicates",d)