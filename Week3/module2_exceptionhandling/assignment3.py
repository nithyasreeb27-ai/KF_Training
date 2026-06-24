balance=5000
pin=1234
statement=""
attempt=0
withdrawal_limit=20000

class Insufficient_balance(Exception):
    pass
class Minimum_balance(Exception):
    pass
class Withdrawal_limit(Exception):
    pass

while(attempt<3):
    try:
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
                    else:
                        print("Deposit should be positive number")
                        continue
                elif(c==3):
                    withdraw=int(input("enter withdraw:"))
                    try:
                        if(withdraw<0):
                            raise ValueError("Withdrawal amount must be positive")
                    except ValueError as v:
                        print(v)
                        continue
                    if(balance<withdraw):
                        raise Insufficient_balance("Insufficient balance")
                    elif(balance-withdraw<=5000):
                        raise Minimum_balance("Minimum balance should be maintained")
                    elif(withdrawn_today+withdraw>=withdrawal_limit):
                        raise Withdrawal_limit("Withdrawal limit exceeds")
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
    except ValueError:
        print("Enter correct value")
    except Insufficient_balance as i:
        print(i)
    except Minimum_balance as m:
        print(m)
    except Withdrawal_limit as w:
        print(w)