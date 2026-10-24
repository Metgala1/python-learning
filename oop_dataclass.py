from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int

product1 = Product("Laptop", 500000)
product2 = Product("Laptop", 500000)
product3 = Product("Phone", 250000)

print(product1 == product2)
print(product1 is product2)