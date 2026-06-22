# # Pattern 1

# with open("Week3/file.txt","r") as file:
#     file=file.read()
# with open("Week3/new.txt","w") as new:
#     new.write(file)
# with open("Week3/new.txt","r") as new:
#     print(new.read())

# Pattern 2

with open("Week3/file.txt","r") as file:
    with open("Week3/new.txt","w") as new:
        for i in file:
            new.write(i)
with open("Week3/new.txt","r") as new:
    print(new.read())