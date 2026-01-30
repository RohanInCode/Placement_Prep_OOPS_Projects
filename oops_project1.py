class BankAccount:
    def __init__(self,acc_no,name,balance):
        self.acc_no =acc_no
        self.name=name
        self._balance=balance

    def deposit(self,amount):
        self._balance+=amount
        return self._balance
    def withdraw(self,amount):
        if amount<=self._balance:
            self._balance-=amount
            return self._balance
        else:
            return "Insufficient balance"
    def get_balance(self):
        return self._balance
    def calculate_interest(self):
        pass


class SavingAccount(BankAccount):
        def calculate_interest(self):
            interest=self._balance*0.04
            return interest
        
class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return 0

class BankApp:
    def __init__(self):
        self.account=None
    def create_account (self,acc_no,name,balance,acc_type):
        if acc_type=="Savings":
            self.account=SavingAccount(acc_no,name,balance)
        else:
            self.account=CurrentAccount(acc_no,name,balance)
        return "Account created successfully"  
    def deposit_money(self,amount):
        return self.account.deposit(amount)
    def withdraw_money(self,amount):
        return self.account.withdraw(amount)
    def check_balance(self):
        return self.account.get_balance()
    def get_interest(self):
        return self.account.calculate_interest()

app=BankApp()
print(app.create_account(101,"Rohan",10000,"Savings"))
print("Balance after depositing:",app.deposit_money(5000))
print("Balance after withdrawing:",app.withdraw_money(2000))
print("Current Balance:",app.check_balance())
print("Interest Earned:",app.get_interest())