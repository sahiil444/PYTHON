class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_detail(self):
        return f"{self.brand} {self.model}"



my_1st_car = Car("toyata","corolla")
print(my_1st_car.brand)

print(my_1st_car.full_detail())