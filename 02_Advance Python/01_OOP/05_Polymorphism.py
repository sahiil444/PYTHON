#  Demostrate polymorphism by defining a method fuel_type in both car and electricCar classes but with different behaviour

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_detail(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Diesel Or Petrol"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)       
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"
    

my_Car = Car("Tata","Safari")
my_ElectricCar = ElectricCar("Tesla","Tesla S","85WKh")

print(my_Car.fuel_type())
print(my_ElectricCar.fuel_type())
