# Modify the Car class to encapsulate the brand atribute ,making it private ,and provide a getter method for it


class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def full_detail(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + "!!!"

my_1st_car = Car("Toyota","Corolla")

# print(my_1st_car.brand)
print(my_1st_car.get_brand())




