products = [
    {"name": "Keyboard", "price": 15000},
    {"name": "Mouse", "price": 5000},
]

# sorted takes a function (key) to decide the order
cheapest_first = sorted(products, key=lambda p: p["price"])

# map applies a function to every item
names = list(map(lambda p: p["name"], products))

# filter keeps items where the function returns True
expensive = list(filter(lambda p: p["price"] > 10000, products))


def make_multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))  # 20
print(triple(10))  # 30