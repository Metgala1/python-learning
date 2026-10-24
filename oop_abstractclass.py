from abc import ABC , abstractmethod

class Payment(ABC):
    def validate_amount(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        
    @abstractmethod
    def pay(self, amount):
        pass


class MobileMoneyPayment(Payment):
    def pay(self , amount):
        self.validate_amount(amount)
        print(f"Processing Mobile Money Payment of {amount} FCFA")

class CardPayment(Payment):
    def pay(self, amount):
        self.validate_amount(amount)
        print(f"Processing card payment of {amount} FCFA")
        
mobile_money = MobileMoneyPayment()
card = CardPayment()

card.pay(500)
mobile_money.pay(1000)

def checkout(payment_method , amount):
    payment_method.pay(amount)

checkout(mobile_money, 2000)
checkout(card, 7000)

#My excersise

class FileExporter(ABC):
    @abstractmethod
    def export(self, data):
        pass

class CSVExporter(FileExporter):
    def export(self, data):
        print(f"Exporting a {data}")

class JsonExporter(FileExporter):
    def export(self, data):
        print(f"Exporting a {data}")

def export_data(exporter, data):
    exporter.export(data)

export_data(CSVExporter() , "csv")
export_data(JsonExporter(), "json")

#using Protocol interface

from typing import Protocol

class FileExporter(Protocol):
    def export(self , data: str) -> None:
        ...

class CSVExporter:
    def export(self, data: str) -> None:
        print(f"Exporting a {data}")

class JSONExporter:
    def export(self, data):
        print(f"Exporting a {data}")

def export_data(provider: FileExporter, data: str) -> None:
    provider.export(data)

export_data(JSONExporter(), "json")
export_data(CSVExporter(), "csv")
