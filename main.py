products = [
    {"name": "Keyboard", "price": 15000, "quantity": 5},
    {"name": "Mouse", "price": 5000, "quantity": 10},
    {"name": "Monitor", "price": 85000, "quantity": 0},
    {"name": "Headphones", "price": 25000, "quantity": 3},
]

def filter_in_stock(products):
    for product in products:
        if product["quantity"] > 0:
            yield product
            
def filter_expensive(products):
    for product in products:
        if product["price"] > 10000:
            yield product

def get_names(products):
    for product in products:
        yield product["name"]

in_stock = filter_in_stock(products)
expensive = filter_expensive(in_stock)
names = get_names(expensive)

for name in names:
    print(name)


