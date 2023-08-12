#class cat
class Cat:
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Hello there, I am {self.name} and I am {self.age} years old.")
    
    def makeSound(self):
        print("meow")
    

#class dog
class Dog:
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Hello there, I am {self.name} and I am {self.age} years old.")
    
    def makeSound(self):
        print("GRUUUwww")
    
#object
cat1 = Cat("Oggy",3)
dog1 = Dog("Bob", 9)

for animal in (cat1, dog1):
    animal.makeSound()
    animal.info()
    print("-"*45)
