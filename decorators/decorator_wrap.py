from functools import wraps

def my_decorator(original_func):
    @wraps(original_func)
    def wrapper(*args , **kwargs):
        print("Calling original function")
        result = original_func(*args , **kwargs)
        
        return result
    return wrapper

@my_decorator
def multiply(a , b):
    return a * b

print(multiply.__name__)
print(multiply(4,5))