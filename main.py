from functools import wraps

def my_decorator(original_func):
    @wraps(original_func)
    def wrapper():
        print("Before")
        original_func()
        print("After")
    
    return wrapper

@my_decorator
def greet():
    """Greet function"""
    print("Hi, Roger")

greet()
