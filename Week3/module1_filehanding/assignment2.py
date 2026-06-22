with open("Week3/mark.txt","r") as marks:
    lst=[]
    total=0
    for i in marks:
        lst.append(int(i))
        total+=int(i)
    print("Highest mark:",max(lst))
    print("Lowest mark:",min(lst))
    print("Total:",total)
    print("Average:",total/len(lst))