#3 L3

def allow_positive_only(func):
    def wrapper(*args):
        for num in args:
            if num <= 0:
                raise ValueError("Only positive numbers are allowed")
        return func(*args)
    return wrapper
@allow_positive_only
def add(a, b):
    return a + b
# Function call
print(add(10, 5))
