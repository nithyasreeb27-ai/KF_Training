students = [
    ("Ram",80),
    ("John",95),
    ("Abiiiiii",70),
    ("Arunnn",88)
]
print("""Menu:
1. sort by alphabets
2. sort by alphabets descending
3. sort by length of student name
4. sort by length of student name in descending
5. sort by marks
6. sort by marks descending""")
n=int(input("enter choice:"))
match n:
    case 1:
        print(sorted(students))
    case 2:
        print(sorted(students,reverse=True))
    case 3:
        b=sorted(students,key=lambda x:len(x[0]))
        print(b)
    case 4:
        b=sorted(students,key=lambda x:len(x[0]),reverse=True)
        print(b)
    case 5:
        b=sorted((students),key=lambda x:x[1])
        print(b)
    case 6:
        b=sorted((students),key=lambda x:x[1],reverse=True)
        print(b)