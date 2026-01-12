#3.L3
def log_arguments(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args)
        print("Keyword Arguments:", kwargs)
        return func(*args, **kwargs)
    return wrapper

@log_arguments
def add(a, b):
    return a + b

print("Result:", add(10, 20))
