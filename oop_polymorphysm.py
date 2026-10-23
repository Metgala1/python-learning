class EmailNotification:
    def send(self):
        print("Sending an Email")

class SMSNotifiaction:
    def send(self):
        print("Sending an SMS")


class PushNotification:
    def send(self):
        print("Sending a push notification")

notifications = [
    EmailNotification(),
    SMSNotifiaction(),
    PushNotification()
]

for notification in notifications:
    notification.send()

# Polymorphism through inheritance

class Animal:
    def speak(self):
        print("Some anumal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

def make_animal_speak(animal):
    animal.speak()

make_animal_speak(Animal())
make_animal_speak(Dog())
make_animal_speak(Cat())

# Duck typing 
class PDFDocument:
    def open(self):
        print("Opening a PDF document")

class MusicPlayer:
    def open(self):
        print("Opening a music player")
class WebBrowser:
    def open(self):
        print("Opening a web browser")

def open_item(item):
    item.open()

open_item(PDFDocument())
open_item(MusicPlayer())
open_item(WebBrowser())


class Payment:
    def process(self):
        print("Processing payment")

class CarPayment(Payment):
    def process(self):
        print("Processing car payment")
class MobileMoneyPayment(Payment):
    def process(self):
        print("processing mobile money payment")

def process_payment(process):
    process.process()

process_payment(Payment())
process_payment(CarPayment())
process_payment(MobileMoneyPayment())