class Bank:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def view_balance(self):
        return (f"Customer Name:{self.owner}\nBalance Amount:{self.balance}")
    
    def deposit(self,deposit):
        self.balance = self.balance + deposit
        return (f"Customer Name:{self.owner}\nBalance Amount:{self.balance}")
    
    def debited(self,debit):
        if self.balance < debit:
            return "INSUFFICIENT BALANCE"
        else:
            self.balance = self.balance - debit
            return (f"Customer Name:{self.owner}\nBalance Amount:{self.balance}")
        
sanju = Bank('Sanju', 3000)

print(sanju.deposit(200))
print(sanju.debited(340))