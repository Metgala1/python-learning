#using typeVar
from typing import TypeVar
T = TypeVar("T")

def get_first(items: list[T]) -> T:
    if not items:
        return None
    return item[0]

names = ["Roger", "David", "John"]
numbers = [10,20,30]

first_name = get_first(names)
first_number = get_first(numbers)

print(first_name)
print(first_number)

#Modern generic synthax in python
def get_first[T](items: list[T]) -> T:
    if not items:
        return None
    return items[0]

get_first()

#Type checking by capacity
class EmailNotification:
    def send(self) -> None:
        print("Sending email...")

class SMSNotification:
    def send(self) -> None:
        print("Sending SMS...")

def notify(notification):
    notification.send()