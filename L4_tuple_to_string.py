#4. program to convert a tuple of string

string_tuple = ('1', '2', '3', '4', '5')
int_tuple = tuple(int(x) for x in string_tuple)
print("Integer tuple:", int_tuple)
