# Public and private methods
class Account:
    def __init__(self, customers, number, balance):
        self.customers = customers
        self.number = number
        self.balance = balance

    def __generate_extract(self):
        print(f"Number: {self.number}\nBalance: {self.balance}")