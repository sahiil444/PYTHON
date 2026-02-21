class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model

    def full_detail(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand
    
    @property
    def model(self):
        return self.__model

my_car = Car("TATA","Safari")
# my_car.model = "City"  
# jabtak property Decorater nhi use kiye the tab tak ham model ko private krne ke baad bhi change kar paa rahe the and ham chahte ye hai ki hm read kr paye change na kar paye model ko

print(my_car.model)