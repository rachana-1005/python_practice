#3.Program to calculate the average value

numbers = (10, 20, 30, 40, 50)
total = 0
for num in numbers:
    total = total + num
average = total / len(numbers)
print("Average value:", average)
