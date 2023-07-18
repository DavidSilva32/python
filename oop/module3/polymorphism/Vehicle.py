# Another exemple of polymorphism
# Create vehicle and eletric vehicle class with method rotate

class Vehicle:
    def rotate(self):
        print("Reduce fuel consumption!")

class ElectricVehicle(Vehicle):
    def rotate(self):
        super().rotate()
        print("This vehicle uses electricity!")

# Create an instance of electric vehicle

my_vehicle = ElectricVehicle()
my_vehicle.rotate()