# Object Oriented Programming

# Exemple
class Person:
    def __init__(self, name, address):
        self.set_name(name)
        self.set_address(address)

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

person1 = Person("Maria", "Street 0123")    
person2 = Person("João", "Street 5678")

print(f"Name: {person1.get_name()}, Address: {person1.get_address()}")
print(f"Name: {person2.get_name()}, Address: {person2.get_address()}")