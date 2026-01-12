#3.L3
def positive_only(func):
    def wrapper(n):
        if n > 0:
            return func(n)
        else:
            print("Only positive numbers are allowed")
    return wrapper

@positive_only
def square(n):
    print("Square:", n * n)

square(5)
square(-3)
