class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(f"{self.name} says:Woof!")
my_dog=Dog("Buddy",3)
you_dog=Dog("Luna",1)
print(my_dog.name)
print(my_dog.age)
my_dog.bark()
my_dog.age=4
print(my_dog.age)
