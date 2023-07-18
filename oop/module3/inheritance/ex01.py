# Exemple of inheritance
class SumMultiply:
    # A simple exemple of overload
    def __init__(self, a, b, y=0):
        self.a = a
        self.b = b
        self.y = y

    def sum(self):
        return self.a + self.b + self.y

    def multiply(self):
        return self.a * self.b * self.y

class Derivative(SumMultiply):
    def subtract(self):
        return self.a - self.b - self.y
    
    def divide(self):
        return self.a / self.b / self.y
    
derivative = Derivative(10,20)
print(f"The sum of the variables is: {derivative.sum()}")
print(issubclass(Derivative, SumMultiply))            