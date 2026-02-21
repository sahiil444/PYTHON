# Create a ElectricCar class that inherits from the Car class and has a additonal atribute(variable) battery_size

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_detail(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)       
        self.battery_size = battery_size


# my_1st_car = Car("Toyota","Corolla")
# print(my_1st_car.brand)
# print(my_1st_car.full_detail())

my_1st_ElectricCar = ElectricCar("Tesla","Tesla S","85KWh")
# print(my_1st_ElectricCar.battery_size)
print(my_1st_ElectricCar.full_detail())