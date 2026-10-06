def calculate_discount(price, percentage):
    """
    Calculate a discounted price.

    price: Original price.
    percentage: Discount percentage.

    Returns:
        The final price after applying the discount.
    """
    discount = price * percentage / 100
    return price - discount

print(calculate_discount.__doc__)