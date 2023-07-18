from Extract import Extract
from datetime import datetime


class Account:
    def __init__(self, customers, number, balance):
        self.customers = customers
        self.number = number
        self.balance = balance
        self.extract = Extract()

    def deposit(self, value):
        self.balance += value
        self.extract.transactions.append(["DEPOSIT", value, "Date", datetime.today()])

    def withdraw(self, value):
        try:
            if self.balance > value:
                self.balance -= value
                self.extract.transactions.append(["WITHDRAW", value, "Date", datetime.today()])
                return print("Withdraw realized successfully!")
            else:
                return print("Insufficient funds!")
        except ValueError:
            return print("Enter a number!")

    def transfer_value(self, destinationAccount, value):
        try:
            if self.balance > value:
                destinationAccount.deposit(value)
                self.balance -= value
                self.extract.transactions.append(["TRANSFER", value, "Date", datetime.today()])
                return print(
                    f"Transfer to the account{destinationAccount.number} realized successfully!"
                )
            else:
                return print("There is not enough value!")
        except:
            print("Enter a number")

    def generate_balance(self):
        if self.customers == []:
            print(
                f"Holders names: {self.customers[0].name}, {self.customers[1].name}\n{self.customers[0].name}'s Address: {self.customers[0].address}, {self.customers[1].name}'s Address: {self.customers[1].address}\nNumber: {self.number}\nBalance: {self.balance}\n"
            )
        else:
            print(
                f"Holders name: {self.customers.name}\n{self.customers.name}'s Address: {self.customers.address}\nNumber: {self.number}\nBalance: {self.balance}\n"
            )