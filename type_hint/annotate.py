#Annotating a type to variables
name: str = "Roger"
age: int = 25
height: float = 1.75
is_student: bool = True

#Annotating a function
def calculate_total(price: float, quantity: int):
    return price * quantity

#Annotating a functions return value
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

#functions that return nothing 
def display_message(message: str) -> None:
    print(message)
    
#Type annotation in real application
def create_product(
    name: str,
    price: float,
    quantity: int
) -> None:
    print(f"Creating: {name}")
    print(f"Price: {price}")
    print(f"Qunatity: {quantity}")

#annotating lis
product: list = [
    "Macbook",
    "iphone",
    "ipad"
]

prices: list[float] = [
    1200.50,
    999.99,
    750.00
]

#another function annotation
def get_products() -> list[str]:
    return ["Macbook", "iphone", "ipad"]

#Annotating a list of dictionaries
products: list[dict[str, str]] = [
    {
        "name": "Mackbook",
        "categories": "Computer"
    },
    {
        "name": "iphone",
        "categories": "Phone"
    }
]

#Annotating tuples
user = tuple[str , int] = ("Roger", 25)

#Backend example
def get_products() -> list[dict[str, str | float | int]]:
    return {
        "name": "Macbook",
        "price": 1200.50,
        "quantity": 5
    }
    
#Dealing with optional
from typing import Optional
user_name: Optional[str] = "Roger"

#Equivalent to 
user_name: str | None = "Roger"

#Annotating function that may return None
def get_user(user_id: str) -> str | None:
    if user_id == 1:
        return "Roger"
    return None

#union type 
customer_id: int | str = 105
customer_id: int | str = "CUS-105"

#union type for functions
def get_customer(customer_id: int | str) -> str:
    return f"Finding customer: {customer_id}"

#Union with more than two values
product_price: int | float | str = 1200
product_price = 1200.50
product_price = "1200.50"

#Literal types
from typing import Literal
def update_order_status(status: Literal["pending", "Processing", "shipped", "delivered"]) -> None:
    print(f"Order status: {status}")
    
#using literals
update_order_status("pending")
update_order_status("shipped")

