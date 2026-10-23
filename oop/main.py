class Student:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self , new_age):
        if new_age < 0:
            raise ValueError("Age cannot be negative")
        self._age = new_age

student = Student(20)
student.age = 26

print(student.age)