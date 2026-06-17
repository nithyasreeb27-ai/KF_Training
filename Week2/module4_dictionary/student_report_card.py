d={
    101:{"name":"a","maths":98,"science":95,"english":92},
    102:{"name":"b","maths":96,"science":91,"english":93},
    103:{"name":"c","maths":92,"science":99,"english":89},
    104:{"name":"d","maths":94,"science":90,"english":85}
}
n=int(input("enter student number:"))
if(n not in d):
    print("Invalid entry")
else:
    print("*********************************")
    print("Report Card".center(30))
    print("*********************************")
    for key,value in d.items():
        if(key==n):
            print("Student id:",key)
            print("Name:",value["name"])
            print("\nSubject and its marks:\n")
            mrks=[]
            for sub,mrk in value.items():
                if(sub!="name"):
                    mrks.append(mrk)
                    print(sub,":",value[sub])
                    if(value[sub]>=90):
                        print("Grade: A")
                    elif(value[sub]>=75):
                        print("Grade: B")
                    elif(value[sub]>50):
                        print("Grade: C")
                    elif(value[sub]>35):
                        print("Grade: D")
                    else:
                        print("fail")
            print("\nOverall information:\n")
            total=0
            for key2,value2 in value.items():
                if(type(value2)==int):
                    total+=value2
            print("Total out of 300:",total)
            avg=round(total/3,2)
            print("Average mark:",avg)
            if(avg>=90):
                print("Overall Grade: A")
            elif(avg>=75):
                print("Overall Grade: B")
            elif(avg>50):
                print("Overall Grade: C")
            elif(avg>35):
                print("Overall Grade: D")
            else:
                print("fail")