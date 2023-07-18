# Create SavingsAccount class with account"s remuneration method
from datetime import datetime

class SavingsAccount:
    def __init__(self, remunerationRate):
        self.remunerationRate = remunerationRate
        self.openingDate = datetime.today()

    def account_remuneration(self):
        self.balance += self.balance * self.remunerationRate