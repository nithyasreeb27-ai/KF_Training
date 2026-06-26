class Bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def display_balance(self):
        return self.balance
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Depositied")
        
    def withdraw(self,amount):
        if(amount<=self.balance):
            self.balance=self.balance-amount
            print("Withdrawn")
        else:
            print("withdrawal is more than balance")

def get_input():
    holder=Bankaccount("a",5000)
    while True:
        print("""Menu:
    1. Check balance
    2. Deposit
    3. Withdraw
    4. Exit""")
        choice=int(input("Enter choice:"))
        if choice==1:
            print("balance:",holder.display_balance())
        elif choice==2:
            amount=int(input("Enter value deposit:")) 
            holder.deposit(amount)
            print("New balance:",holder.balance)
        elif choice==3:
            amount=int(input("Enter value withdraw:"))
            holder.withdraw(amount)
            print("New balance:",holder.balance)
        elif choice==4:
            print("Thank you")
            break
        else:
            print("Wrong input")

get_input()