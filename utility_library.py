def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the result of dividing a by b."""
    return a / b


def calculate_percentage(value, percentage=10):
    """Calculate a percentage of a value."""
    return value * percentage / 100


def calculate_total(price, quantity=1):
    """Calculate the total cost of a product."""
    return price * quantity


def apply_discount(price, discount_percentage):
    """Return the price after applying a discount."""
    discount = price * discount_percentage / 100
    return price - discount


def calculate_order_total(
    price,
    quantity,
    discount_percentage=0
):
    """Calculate the final order total."""

    subtotal = calculate_total(price, quantity)

    return apply_discount(
        subtotal,
        discount_percentage
    )


def sum_prices(*prices):
    """Return the sum of any number of prices."""

    total = 0

    for price in prices:
        total += price

    return total


def create_product(name, price, **details):
    """Create and return a product dictionary."""

    product = {
        "name": name,
        "price": price
    }

    product.update(details)

    return product