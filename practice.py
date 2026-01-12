Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={[1,2,3]99,'a':44}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
d={[1,2,3]:99,'a':44}
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    d={[1,2,3]:99,'a':44}
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
l=[1,2,3]
d={i:i*i,for i in l}
SyntaxError: invalid syntax
l=[1,2,3]

d={i:i*i for i in l}
print(d)
{1: 1, 2: 4, 3: 9}
num=[10,40,20,30,50]
len(num)
5
max(num)
50
min(num)
10
sum(num)
150
sorted(num)
[10, 20, 30, 40, 50]
list(reverse(num))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list(reverse(num))
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
list(reversed(num))
[50, 30, 20, 40, 10]
num.append(80)
print(num)
[10, 40, 20, 30, 50, 80]
num.insert(4,78)
print(num)
[10, 40, 20, 30, 78, 50, 80]
num.extend([6,7])
num
[10, 40, 20, 30, 78, 50, 80, 6, 7]
num.remove(40)
num
[10, 20, 30, 78, 50, 80, 6, 7]
>>> num.pop(6)
6
>>> num.clear()
>>> num
[]
>>> squares=[]
>>> squares_comp=[i*i for i in range(1,6)]
>>> print(squares_comp)
[1, 4, 9, 16, 25]
>>> nums=[1,2,3,4,4,5]
>>> unique={n*n for i in nums}
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    unique={n*n for i in nums}
NameError: name 'n' is not defined
>>> squares=[]
>>> nums[1,2,3,4,4,5]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    nums[1,2,3,4,4,5]
TypeError: list indices must be integers or slices, not tuple
>>> nums=[1,2,3,4,4,5]
>>> unique={n*n for n in nums}
>>> unique
{1, 4, 9, 16, 25}
>>> t1=tuple()
>>> t1
()
