class Automobile:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"The {self.brand} is starting.")

    def brake(self):
        print(f"The {self.brand} is braking.")

class Car(Automobile):
    pass

class Bike(Automobile):
    pass

car = Car("Toyota")
bike = Bike("Honda")

car.start()  
car.brake() 