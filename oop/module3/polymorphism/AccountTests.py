# import file from another folder
import sys

sys.path.insert(0, 'C:\\Users\\david\\OneDrive\\Documentos\\estacio\\estudos\\python\\oop\\module2\\aggregation')

from Accounts import Account
from Customers import Client
from SavingsAccount import SavingsAccount

class RemuneratedSavingsAccount(Account, SavingsAccount):
    def __init__(self, remunerationRate, customers, number, balance, monthlyRate):
        Account.__init__(self, customers, number, balance)
        SavingsAccount.__init__(self, remunerationRate)
        self.monthlyRate = monthlyRate

    def remunarateAccount(self):
        self.balance += self.balance * (self.remunerationRate/30)
        self.balance -=  self.monthlyRate 

# Instance the classes 

client1 = Client(123,"Joao","Street X") 
client2 = Client(456, "Maria", "Street W")  

account1 = Account([client1,client2],1,2000)

savingsAccount1 = SavingsAccount(0.1)
remuneratedAccount1 = RemuneratedSavingsAccount(0.1,client1,5,1000,5)  
remuneratedAccount1.remunarateAccount()
remuneratedAccount1.generate_balance()