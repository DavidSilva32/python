# composition to each account

class Extract:
    def __init__(self):
        self.transactions = []

    def generate_extract(self, accountNumber):
        print(f"Extract: {accountNumber}")
        for t in self.transactions:
            print(f"{t[0]:15s} {t[1]:10.2f} {t[2]:10s} {t[3].strftime('%d/%m/%y')}")
        print("\n")