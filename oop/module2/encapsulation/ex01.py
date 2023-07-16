# Public and Private attributes
class Account:
    def __init__(self, number):
        self.__number = number
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, balance):
        if self.balance < 0:
            print("Invalid balance!")
        else:
            self.__balance = balance    

def main():
    account = Account(1)
    account.balance = 1000 # using the @alance.setter
    print(f"Account balance: {account.balance}") # using the @property

main()
