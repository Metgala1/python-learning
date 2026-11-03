from typing import Protocol

class Notification(Protocol):
    def send(self) -> None:
        ...

class EmailNotification():
    def send(self) -> None:
        print("Sending email...")

class SMSNotification():
    def send(self) -> None:
        print("Sending SMS...")


def notify(notification: Notification) -> None:
    notification.send()


