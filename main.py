class Engine:
    def start(set):
        print("Standard engine started")

class ElectricMotor:
    def start(self):
        print("Electric motor started silently")


class Car:
    def __init__(self, engine):
        self.engine = engine
    
    def start(self):
        self.engine.start()

petrol_car = Car(Engine())
electric_car = Car(ElectricMotor())

petrol_car.start()
electric_car.start()