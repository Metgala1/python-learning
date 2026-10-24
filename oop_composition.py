class Engine:
    def start(self):
        print("Standard engine started.")


class ElectricMotor:
    def start(self):
        print("Electric motor started silently.")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
        
#A class stores and uses another class that's composition instead of inheriting 
#Exercise
class CPU:
    def run(self):
        print("CPU is running")

class Computer:
    def __init__(self, cpu):
        self.cpu = cpu
    def start(self):
        self.cpu.run()

mac = Computer(CPU())
mac.start()