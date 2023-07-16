from Accounts import Account
from Customers import Client
from Bank import Bank

customers = [
    Client(123, "Lisa", "Street 1"),
    Client(456, "Bart", "Street 2"),
]  # Client list
accounts = [Account([customers[0], customers[1]], 1, 0)]  # Account list
bank = Bank(customers, accounts)

accounts[0].generate_balance()
accounts[0].deposit(1500)
accounts[0].withdraw(500)
accounts[0].generate_balance()
accounts[0].extract.generate_extract(accounts[0].number)

customers.append(Client(765, "John", "Street 23"))  # Adding new client
customers.append(Client(432, "Maria", "Street 23"))  # Adding new client
accounts.append(Account([customers[2], customers[3]], 2, 0))  # Adding new account

accounts[0].transfer_value(accounts[1], 500)
accounts[1].generate_balance()
accounts[1].extract.generate_extract(accounts[1].number)
accounts[0].extract.generate_extract(accounts[0].number)

print(bank.show_customers())
print(bank.show_accounts())