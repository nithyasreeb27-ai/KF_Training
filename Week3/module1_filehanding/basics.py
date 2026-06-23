# all data

with open("Week3/file.txt","r") as file:
    data=file.read()
print(data)

# Line by line

with open("Week3/file.txt","r") as file:
    for line in file:
        print(line)

# Counting pattern

count=0
with open("Week3/file.txt") as file:
    for line in file:
        count+=1
print(count)

# Total

total=0
with open("Week3/mark.txt","r") as marks:
    for mark in marks:
        total+=int(mark)
print(total)

# Search

a="Ram"
with open("Week3/file.txt","r") as file:
    data=file.read()
if a in data:
    print("Found")

a="Ram"
with open("Week3/file.txt","r") as file:
    for line in file:
        if a in line:
            print("Found")

# Max/Min

with open("Week3/mark.txt","r") as marks:
    l=[]
    for mark in marks:
        l.append(int(mark))
    high=max(l)
    print(high)

# Append 

# with open("Week3/mark.txt","a") as marks:
#     new=marks.write("\n100")
# with open("Week3/mark.txt","r") as marks:
#     print(marks.read())

# Copy or transform

with open("Week3/file.txt","r") as file:
    with open("Week3/new.txt","w") as new:
        old=file.read()
        for i in old:
            new.write(i.upper())
with open("Week3/new.txt","r") as new:
    print(new.read())

# read and write

with open("Week3/new.txt","r+") as rw:
    rw.read()
    rw.seek(4)
    rw.write("\nRAJ")
    rw.seek(0)
    print(rw.read())

# Repalce

with open("Week3/file.txt","r") as file:
    data=file.read()
    data=data.replace("Abi","sai")
    with open("Week3/file.txt","w") as new:
        new.write(data)
with open("Week3/file.txt","r") as data:
    print(data.read())