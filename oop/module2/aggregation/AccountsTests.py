from Accounts import Account
from Customers import Client

customers = [
    Client(123, "Lisa", "Street 1"),
    Client(456, "Bart", "Street 2"),
]  # Client list
accounts = [Account([customers[0], customers[1]], 1, 0)]  # Account list

accounts[0].generate_extract()
accounts[0].deposit(1500)
accounts[0].withdraw(500)
accounts[0].generate_extract()

customers.append(Client(765, "John", "Street 23"))  # Adding new client
customers.append(Client(432, "Maria", "Street 23"))  # Adding new client
accounts.append(Account([customers[2], customers[3]], 2, 0))  # Adding new account

accounts[0].transfer_value(accounts[1], 500)
accounts[1].generate_extract()
