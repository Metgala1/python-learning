def make_greeter(name):
    def greet():
        print(f"Hello, {name}!")

    return greet


greet_anna = make_greeter("Anna")
greet_david = make_greeter("David")

greet_anna()
greet_david()

#Closures are functions that remember variables from the sorrounding functions they are created in
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        print(count)

    return counter


my_counter = make_counter()

my_counter()
my_counter()
my_counter()