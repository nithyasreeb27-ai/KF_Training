# Notes App

print("""Menu:
1.View
2.Add
3.Exit""")


while True:
    n=int(input("Enter number:"))
    match n:
        case 1:
            with open("Week3/file.txt","r") as file:
                print(file.read())
        case 2:
            add=input("Adding note:")
            with open("Week3/file.txt","a") as file:
                file=file.write("\n"+add)
        case 3:
            print("ThankYou")
            break