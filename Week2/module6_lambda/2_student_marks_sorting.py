def sort_alph(n):
    # b=[]
    # for i in students:
    #     b.append((i["name"]))
    # print(sorted(b))
    print(sorted(list(map(lambda x:x["name"],students))))

def sort_alpha_desc(n):
    print(sorted(list(map(lambda x:x["name"],students)),reverse=True))

def sort_len(n):
    print(sorted(list(map(lambda x:x["name"],students)),key=len))

def sort_len_desc(n):
    print(sorted(list(map(lambda x:x["name"],students)),key=len,reverse=True))

def sort_phy(n):
     # print(sorted(list(map(lambda x:x["phy"],students))))
    # b=list(map(lambda x: x["name"],sorted(students,key=lambda x:x["phy"])))
    # print(b)
    new=sorted(students,key=lambda x:x["phy"])
    for student in new:
        print(student["name"],":",student["phy"])

def sort_chem(n):
    new=sorted(students,key=lambda x:x["chem"])
    for student in new:
        print(student["name"],":",student["chem"])
    
def sort_math(n):
    new=sorted(students,key=lambda x:x["math"])
    for student in new:
        print(student["name"],":",student["math"])

def menu():
    match n:
        case 1:
            return sort_alph(students)
        case 2:
            return sort_alpha_desc(students)
        case 3:
            return sort_len(students)
        case 4:
            return sort_len_desc(students)
        case 5:
            return sort_phy(students)
        case 6:
            return sort_chem(students)            
        case 7:
            return sort_math(students)

students = [
    {
        "name":"Ram",
        "phy":80,
        "chem":90,
        "math":85
    },
    {
        "name":"John",
        "phy":95,
        "chem":70,
        "math":88
    },
    {
        "name":"Abiiii",
        "phy":70,
        "chem":85,
        "math":92
    }
]

print("""Menu:
1. sort by alphabets
2. sort by alphabets descending
3. sort by length of student name
4. sort by length of student name in descending
5. sort by phy
6. sort by chem
7. sort by math""")
n=int(input("enter choice:"))
menu()