class Bank:
    def __init__(self, customers, accounts):
        self.customers = customers
        self.accounts = accounts

    def show_customers(self):
        for c in self.customers:
            print(f"Name: {c.name}, CPF: {c.cpf}, Address: {c.address}")
        print("\n")  

    def show_accounts(self):
        for a in self.accounts:
            print(f"Holders names: {a.customers[0].name}, {a.customers[1].name}\nAccount number: {a.number}, Balance: {a.balance}")
        print("\n")       
