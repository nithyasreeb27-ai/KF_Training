# n=int(input("enter number of students:"))
# d={}
# for i in range(n):
#     name=input("enter name:")
#     marks=list(map(int,input("enter marks:").split()))
#     d[name]=marks

# d={
#     "a":[90, 98, 99],
#     "b":[99, 97, 95]
# }

# student=input("enter student name:")
# if student in d.keys():
#     print(d[student])
# else:
#     print("Incorrect entry")


d={
    101:{"name":"a","maths":98,"science":95,"english":92},
    102:{"name":"b","maths":96,"science":91,"english":93}
}
print("""Requirement:
    1. everyone's mark details
    2. mark detail based on id
    3. marks detail based on name
      """)
n=int(input("enter your choice:"))
if(n==1):
    for key,value in d.items():
        print("roll:",key)
        print("name:",d[key]["name"])
        print("maths:",d[key]["maths"])
        print("science:",d[key]["science"])
        print("english:",d[key]["english"])
    
elif(n==2):
    student_id=int(input("enter:"))
    if student_id in d.keys():
        print(d[student_id])
    else:
        print("invalid entry")

elif(n==3):
    student_name=input("enter:")
    for key,value in d.items():
        if (value["name"]==student_name):
            print(d[key])
    else:
        print("invalid entry")