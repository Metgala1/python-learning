def outer(greeting):
    message = greeting
    def inner():
        print(message)
    return inner

my_function = outer("Hi")
my_function()