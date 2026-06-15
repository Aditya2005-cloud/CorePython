# ATM Simulator Features:

# PIN verification
# Deposit
# Withdraw
# Transaction history

class Bank:
    def __init__(self,name,bname,amount,pin):
        self.name=name
        self.bname=bname
        self.amount=amount
        self.pin=pin
        # added
        self.history=[]

    def deposit(self):
            user_pin=int(input("Enter the pin to use: "))
            if self.pin==user_pin:
                print(f"{self.name} can use the atm to deposit: ")
                user_deposit_amount=int(input("enter the amount to deposit: "))
                self.amount=self.amount+user_deposit_amount
                # added
                self.history.append(f"Deposited ₹{user_deposit_amount}")
            else:
                print("u have entered the wrong pin")
            print(f"ur updated balance is {self.amount}")

    def withdraw(self):
            user_pin=int(input("Enter the pin to use: "))
            if self.pin==user_pin:
                print(f"{self.name} can use the atm to withdraw: ")
                user_withdraw_amount=int(input("enter the amount to withdraw: "))
                if user_withdraw_amount<=self.amount:
                    self.amount=self.amount-user_withdraw_amount
                    # added
                    self.history.append(f"Withdrawn ₹{user_withdraw_amount}")
                else:
                    print("insufficient balance")
            else:
                print("u have entered the wrong pin")
            print(f"ur updated balance is {self.amount}")

    def show_balance(self):
        print(f"u r current balance is = {self.amount}")

    def transaction_history(self):
        if len(self.history)==0:
            print("No transactions yet")
        else:
            print("\nTransaction History")
            for i in self.history:
                print(i)


name=input("Enter you name: ")
bname=input("Enter which bank u want: ")
amount=int(input("Enter the aount u want to submit in bank: "))
pin=int(input("Enter the pin no: "))
user1=Bank(name,bname,amount,pin)
user1.show_balance()
user1.deposit()
user1.withdraw()
# added
user1.transaction_history()