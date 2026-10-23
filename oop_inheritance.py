class Animal:
    def __init__(self , name):
        self.name = name
    def introduce(self):
        print(f"My name us {self.name}")

class Dog(Animal):
    def introduce(self):
        super().introduce()
        print("I am a dog")
    
dog = Dog("Buddy")
dog.introduce()