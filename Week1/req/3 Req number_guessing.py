import random
num=random.randint(1,10)
attempt=0
while(attempt<3):
    n=int(input("enter a number between 1 and 10:"))
    if(num==n):
        print("Correct guess")
        break
    elif(num>n):
        print("the number you chose is low")
    else:
        print("the number you chose is high")
    attempt+=1
