#Comments
# Calculate the discounted price
price = 1000
discounted_price = price * 0.9

#Add 10 to price
price = price + 10

#Docstrings
def calculate_total(price, quantity):
    """Calculate the total price of an order."""
    return price * quantity

print(calculate_total.__doc__)

#Writing better function documentation
def calculate_total(price: float, quantity: int) -> float:
    """
    Calculate the total price of an order.

    Args:
        price: Price of one item.
        quantity: Number of items ordered.

    Returns:
        Total price before taxes.
    """
    return price * quantity

#Documenting classes
class BankAccount:
    """
    Represent a customer's bank account.

    Attributes:
        owner: Name of the account owner.
        balance: Current account balance.
    """

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        self.balance += amount

#Documenting an entire module
"""
Order management operations.

This module contains functions for calculating
order totals and applying discounts.
"""


def calculate_total(price, quantity):
    """Calculate an order's total before taxes."""
    return price * quantity


def apply_discount(total, discount):
    """Apply a percentage discount to an order."""
    return total * (1 - discount / 100)