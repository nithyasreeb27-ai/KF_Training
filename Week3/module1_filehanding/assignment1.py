with open("Week3/student.txt","r") as students:
    print(students.read())
    students.seek(0)
    count=0
    for student in students:
        count+=1
    print("Total:",count)