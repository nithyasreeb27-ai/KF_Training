balance=5000
pin=1234
statement=""
attempt=0
withdrawal_limit=20000
while(attempt<3):
    n=int(input("enter pin:"))
    if(n!=pin):
        attempt+=1
        if(attempt<=2):
            print("Wrong pin! try again")
        else:
            print("only 3 attempts are allowed")
    if(n==pin):
        withdrawn_today=0
        while True:
            print("""
    1. Balance
    2. Deposit
    3. Withdraw
    4. Mini statement
    5. Exit""")
            c=int(input("enter choice:"))
            if (c==1):
                print(balance)
            elif(c==2):
                dep=int(input("enter deposit:"))
                if(dep>0):
                    balance+=dep
                    statement+=(f"deposited {dep}\n")
                    print("deposited")
            elif(c==3):
                withdraw=int(input("enter withraw:"))
                if(balance<withdraw):
                    print("Insufficient Balance")
                elif(balance-withdraw<=5000):
                    print("Minimum balance should be maintained")
                elif(withdrawn_today+withdraw>=withdrawal_limit):
                    print("Withdrawal limit exceeds")
                else:
                    balance-=withdraw
                    withdrawn_today+=withdraw
                    statement+=(f"withdrawn {withdraw}\n")
                    print("Withdrawn")
            elif(c==4):
                print(statement)
            elif(c==5):
                print("Thank you")
                break
            else:
                print("invalid entry")
        break