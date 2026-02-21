# Add a statice method to the car class that return the general description of a car 


class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_detail(self):
        return f"{self.brand} {self.model}"
    
    @staticmethod
    def description():
        return "Cars Are Cool Haa Haa Haa !!!!"

my_car = Car("TATA","Safari1")

# print(my_car.description())
print(Car.description())