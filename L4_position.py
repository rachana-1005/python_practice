#3.list of elements

elements = [10, 20, 30, 40, 50]
print("List:",elements)
items = input("Enter the element to add: ")
position = int(input("Enter the position (index): "))
elements.insert(position, items)
print("Updated list:", elements)

