class EmailNotification:
    def send(self) -> None:
        print("Sending email...")

class SMSNotification:
    def send(self) -> None:
        print("Sending SMS...")

def notify(notification):
    notification.send()

notify(SMSNotification())

set = set()
