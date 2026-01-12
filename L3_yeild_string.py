#5.Generator that takes a string and yields each character in uppercase

def uppercase_generator(s):
    for ch in s:
        yield ch.upper()
for char in uppercase_generator("Rachana"):
    print(char)
