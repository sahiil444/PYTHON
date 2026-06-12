#  Add a class variable to car that keeps track of number of car created 


class Car:
    Total_Car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.Total_Car += 1

    def full_detail(self):
        return f"{self.brand} {self.model}"
    

Car("TATA","Safari1")
Car("TATA","Safari2")
Car("TATA","Safari3")
Car("TATA","Safari4")

print(Car.Total_Car)