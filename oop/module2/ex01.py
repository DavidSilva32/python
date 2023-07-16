# Builders and Self


class Account:
    def __init__(self, number, cpf, holderName, balance):
        self.number = number
        self.cpf = cpf
        self.holderName = holderName
        self.balance = balance


def main():
    account = Account(1, 1, "Marco", 1000)  # Object being instantiated
    print(f"Name of the account holder: {account.holderName}")
    print(f"Account number: {account.number}")
    print(f"CPF of the account holder: {account.cpf}")
    print(f"Account balance: {account.balance}")


if __name__ == "__main__":
    main()


# class without builder


class A:
    def f(self):
        print("foo")


def main():
    obj_A = A()  # Object being instantiated
    obj_A.f()


if __name__ == "__main__":
    main()
