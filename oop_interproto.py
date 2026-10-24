# from abc import ABC , abstractmethod
# #Abstract method
# class PaymentProvider(ABC):
#     @abstractmethod
#     def pay(self, amount: float) -> None:
#         pass

# class MobileMoney(PaymentProvider):
#     def pay(self, amount: float) -> None:
#         print(f"Processing Mobile Money Payment: {amount}")
        
# momo = MobileMoney()
# momo.pay(5000)

#Protocol method

from typing import Protocol
class PaymentProvider(Protocol):
    def pay(self, amount: float) -> None:
        ...

class MobileMoney:
    def pay(self, amount: float) -> None:
        print(f"Processing Mobile Money payment: {amount}")

class CardPayment:
    def pay(self, amount: float) -> None:
        print(f"Processing card payment: {amount}")
        
def checkout(provider: PaymentProvider , amount: float) -> None:
    provider.pay(amount)

checkout(MobileMoney(), 500)
checkout(CardPayment(), 12000)
