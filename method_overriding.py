from math import pi

class Shape:
    #constructor
    def __init__(self, name):
        self.name = name
        
    def area(self):
        pass
    
    def fact(self):
        return "I am a two-dimensional shape."
    
    def __str__(self):
        return self.name
    
class Square(Shape): #Square class inheriting Shape
    
    def __init__(self, length):
        #calling __init__ function from the parent class Square
        super().__init__("Square")
        self.length = length
        
    def area(self):
        return self.length**2
    
    def fact(self):
        return "There are only 4 90degree angles in a Square."
    
class Circle(Shape):
    #constructor
    def __init__(self, radius):
        #calling __init__ function from the parent class Square
        super().__init__("Circle")
        self.radius = radius
        
    def area(self):
        return pi*self.radius**2
    
s = Square(3)
c = Circle(9)

print(s)
print(c)

print(s.fact())
print(c.fact())

print(s.area())
print(c.area())
        
