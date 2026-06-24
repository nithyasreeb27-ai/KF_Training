try:
    with open("Week3/module2_errorhandling/dem.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File name not found")