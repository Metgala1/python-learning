
products = [
    {"name": "MacBook Air", "price": 1200000},
    {"name": "iPhone", "price": 900000},
    {"name": "AirPods", "price": 150000},
]

expensive_products = (
    product["name"] for product in products if product["price"] > 500000
)

print(list(expensive_products))