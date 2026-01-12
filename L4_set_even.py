#1.program to create set of even numbers

even_numbers = set()
for num in range(1, 21):
    if num%2==0:
        even_numbers.add(num)
print("Even numbers:", even_numbers)


