class Account:
    def __init__(self, customers, number, balance):
        self.customers = customers
        self.number = number
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        try:
            if self.balance > value:
                self.balance -= value
                return print("Withdraw realized successfully!")
            else:
                return print("Insufficient funds!")
        except ValueError:
            return print("Enter a number!")

    def trasnfer_value(self, destinationAccount, value):
        if self.balance > value:
            destinationAccount.deposit(value)
            self.balance -= value
            return print("Transfer realized successfully!")
        else:
            return print("There is not enough value!") 

    def generate_extract(self):
        print(f"Number: {self.number}\nBalance: {self.balance}")             