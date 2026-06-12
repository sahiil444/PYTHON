# create a car class with atribute brand and model. then create a instance of this class 


class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    # def full_detail(self,brand,model):



my_1st_car = Car("toyata","corolla")
print(my_1st_car.brand)
print(my_1st_car.model)