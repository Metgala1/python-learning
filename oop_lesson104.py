
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount to be withdrawn must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount

    def get_balance(self):
        return self._balance


account = BankAccount("Roger", 100_000)


def show_message():
    print(f"{'=' * 6} Welcome to your account {'=' * 6}")
    print("1. To deposit")
    print("2. To withdraw")
    print("3. To check account balance")
    print("4. To exit account")


while True:
    show_message()
    option = input("Select an option: ").strip()

    if option == "1":
        try:
            amount = int(input("Enter deposit amount: "))
            account.deposit(amount)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            print("Deposit successful!")

    elif option == "2":
        try:
            amount = int(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            print("Withdrawal successful!")

    elif option == "3":
        print(f"Account owner: {account.owner}")
        print(f"Your account balance is {account.get_balance():,} FCFA")

    elif option == "4":
        print("Exiting account. Goodbye!")
        break

    else:
        print("Invalid command. Please try again.")

        
