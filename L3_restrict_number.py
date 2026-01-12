#4. Decorator that restricts division by zero

def safe_division(func):
    def wrapper(a, b):
        if b == 0:
            print("Error: Division by zero is not allowed")
        else:
            return func(a, b)
    return wrapper
@safe_division
def divide(a, b):
    return a / b
print(divide(10, 2))
divide(10, 0)
