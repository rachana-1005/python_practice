#4.L3
num=int(input("Enter a number:"))
if num<=1:
        print(f"Not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print(f" Not a prime number")
            break
        else:
            print(f"prime number")
