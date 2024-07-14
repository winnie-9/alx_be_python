class BankAccount:
    def __init__(self, account_balance =0):
        self.account_balance = account_balance


    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
        return self.account_balance
    
    def withdraw(self, amount):
        if self.account_balance <  amount:
            return False
        else:
            self.account_balance = self.account_balance - amount
            return True, self.account_balance
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")