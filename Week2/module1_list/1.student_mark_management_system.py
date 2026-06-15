print("STUDENT MARK MANAGEMENT SYSTEM")
length=int(input("enter number of subjects"))
marks=list(map(int,input("enter marks:").split()))
print("MENU:\n"
"1. Display all marks \n" 
"2. Total marks\n" 
"3. Average of the marks \n" 
"4. Sort marks \n" 
"5. Highest mark \n" 
"6. Lowest mark \n" 
"7. Remove duplicate marks \n" 
"8. Search mark\n"
"9. Exit")
while True:
    n=int(input("enter your choice:"))
    if(n==1):
        print("all marks:",marks)
    elif(n==2):
        total=0
        for i in marks:
            total+=i
        print("Total:",total)
    elif(n==3):
        print("Average:",sum(marks)/length)
    elif(n==4):
        print("sorted list of marks:",sorted(marks))
    elif(n==5):
        print("Maximun mark:",max(marks))
    elif(n==6):
        print("Minimum mark",min(marks))
    elif(n==7):
        d=[]
        for j in marks:
            if j not in d:
                d.append(j)
        print("removed duplicated marks:",d)
    elif(n==8):
        mrk=int(input("enter the mark:"))
        if mrk in marks:
            print(f"found at the index, {marks.index(mrk)}")
    elif(n==9):
        print("Thank you")
        break
    else:
        print("Wrong input")