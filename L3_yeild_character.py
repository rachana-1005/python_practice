#3.Generator that yields characters of a string one by one

def string_characters(s):
    for ch in s:
        yield ch
for c in string_characters("Python"):
    print(c)

