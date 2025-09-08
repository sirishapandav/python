class BankAccount:
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(amount,"amount deposited successfully")
            print(self.balance)
        else:
            print("invalid amount")
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print(amount,"amount with drawn successfully")
            print(self.balance)
        else:
            print("invalid amount")
    def display(self):
        print("balance:",self.balance)
class SavingsAccount(BankAccount):
    def __init__(self, interest_rate):
        super().__init__(1234,1000)          
        self.interest_rate=interest_rate
    def calculate_interest(self):
        interest=self.balance*self.interest_rate/100
        self.deposit(interest)
s=SavingsAccount(5)
s.calculate_interest()
s.deposit(1000)
s.withdraw(500)
s.display()       


    