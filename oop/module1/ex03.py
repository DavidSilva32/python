# Class method and Static method

from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # A class method to create
    # A person object through year of birth
    @classmethod
    def yearOfBirth(cls, name, year):
        return cls(name, date.today().year - year)
    #static method: check if you are legal age
    @staticmethod
    def isOfLegalAge(age):
        return age >= 18
    
person1 = Person("Maria", 26)
person2 = Person.yearOfBirth("Ana", 2006)
print(person1.age)
print(person2.age)
# Print of result
print(Person.isOfLegalAge(17)) 