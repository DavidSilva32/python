# Add the 'folder' directory to the sys.path
import sys

sys.path.insert(0,'C:\\Users\\david\\OneDrive\\Documentos\\estacio\\estudos\\python\\oop\\module2\\aggregation')

# Create subclass special account
from Accounts import Account, datetime
from Customers import Client

class SpecialAccount(Account):
    def __init__(self, customers, number, balance, limit):
        Account.__init__(self, customers, number, balance)
        self.limit = limit

    def withdraw(self, value):
        if (self.balance + self.limit) >= value:
            self.balance -= value
            self.extract.transactions.append("WITHDRAW", value, "Date", datetime.today())
            return True
        
        else:
            print("Insufficient balance")
            return False
        
# instantiate Client, Account and Special account

client1 = Client(123, "John", "Street 1")
client2 = Client(456, "Claire", "Street 1")
client3 = Client(789, "Maria", "Street 2")

account1 = Account({client1,client2}, 1,2000)
account2 = SpecialAccount(client3, 3, 1000, 2000)

account2.deposit(100)
account2.withdraw(3200)
