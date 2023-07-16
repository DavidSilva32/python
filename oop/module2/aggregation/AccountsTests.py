from Accounts import Account
from Customers import Client

client1 = Client(123, "Lisa", "Street 1")
client2 = Client(456, "Bart", "Street 2")
account1 = Account([client1, client2], 1, 0)
account1.generate_extract()
account1.deposit(1500)
account1.withdraw(500)
account1.generate_extract()