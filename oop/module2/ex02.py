# Methods


# Bank simulation
class Account:
    def __init__(self, number, cpf, holderName, balance):
        self.number = number
        self.cpf = cpf
        self.holderName = holderName
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value

    def generate_extract(self):
        print(
            f"Number: {self.number}\nCPF: {self.cpf}\nHolder name: {self.holderName}\nBalance: R${self.balance}"
        )


def main():
    account = Account(1, 1, "David", 1000)
    account.deposit(500)
    account.withdraw(300)
    account.generate_extract()


if __name__ == "__main__":
    main()
