#1 #lab3 1.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = int(input("Enter your choice (1-4): "))
if choice == 1:
    result = num1 + num2
    print(f"Addition of {num1} and {num2} is: {result}")

elif choice == 2:
    result = num1 - num2
    print(f"Subtraction of {num1} and {num2} is: {result}")

elif choice == 3:
    result = num1 * num2
    print(f"Multiplication of {num1} and {num2} is: {result}")

elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print(f"Division of {num1} by {num2} is: {result}")
    else:
        print("Division by zero is not allowed")

else:
    print("Invalid choice")
        
        
