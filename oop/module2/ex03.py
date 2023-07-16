# Methods with return


class Account:
    def __init__(self, number, cpf, holderName, balance):
        self.number = number
        self.cpf = cpf
        self.holderName = holderName
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if self.balance > value:
            self.balance -= value
            return "It was realized"
        else:
            return "It wasn't realized"
        
    def transfer_value(self, destinationAccount, value):
        if self.balance > value:
            destinationAccount.deposit(value)
            self.balance -= value
            return "Transfer realized"
        else:
            return "There is not enough value!"

    def generate_extract(self):
        print(f"\nNumber: {self.number}\nCPF: {self.cpf}\nHolder name: {self.holderName}\nBalance: R${self.balance}")


def main():
    account = Account(1, 1, "Anne", 0)
    account.deposit(300)
    withdraw = account.withdraw(400)
    account.generate_extract()
    print(f"The withdrawal was realized?\n{withdraw}")

if __name__ == "__main__":
    main()