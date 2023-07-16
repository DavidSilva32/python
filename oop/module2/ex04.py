# References between objects in memory

from ex03 import Account

account1 = Account(1, 123, "Marco", 0) # Object being instantiated
account2 = Account(3, 456, "Maria", 0)

account1.deposit(1000)
account1.transfer_value(account2, 500)
print(account1.generate_extract())
print(account2.generate_extract())