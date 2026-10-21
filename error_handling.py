try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    result = first_number / second_number
    print("Result:", result)
except ValueError:
    print("Invalid number")
except Exception:
    print("Something went wrong")
    
file = None

try:
    file = open("tasks.json" , "r" , encoding="utf-8")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The task file does not exist")
finally:
    if file is not None:
        file.close()
        print("File closed")
        

def validate_age(age):
    if age < 0:
        raise ValueError("Age can not be negative.")
    return "Age accepted"

try:
    result = validate_age(-5)
    print(result)
except ValueError as error:
    print("Validation failed:", error)

#Custom exceptions

class InsufficientFundsError(Exception):
    def __init__(self , balance, amount):
        self.balance = balance
        self.amount = amount
        
        super().__init__(
            f"Balance: {balance} FCFA; requested: {amount} FCFA"
        )

def withdraw(balance , amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_amount = withdraw(20_000, 5_000)
    print("Withdrawal successful.")
    print("Remaining balance:", new_amount)
except ValueError as error:
    print("Invalid withdrawl:", error)
except InsufficientFundsError as error:
   print(error)
   print("Available balance:", error.balance)
   print("Requested amount:", error.amount)
   

def calculate_discounted_price(price, discount_percent):
    if price < 0:
        raise ValueError("Price cannot be negative.")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    discount = price * (discount_percent / 100)
    return price - discount


try:
    price = float(input("Enter product price: "))
    discount_percent = float(input("Enter discount percentage: "))
except ValueError:
    print("Please enter valid numeric values.")
else:
    try:
        final_price = calculate_discounted_price(
            price,
            discount_percent
        )
    except ValueError as error:
        print("Could not calculate price:", error)
    else:
        print("Final price:", final_price)