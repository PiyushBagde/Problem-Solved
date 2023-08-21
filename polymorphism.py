
class Polygon:
    def render(self):
        print("Rendering polygon")

class Square(Polygon):
    def renderSquare(self):
        print('Rendering Square')


class Circle:
    def render(self):
        print('Rendering Circle')

s1 = Square()
s1.render() #showing inheritance
s1.renderSquare() 

s2 = Circle()
s2.render() #showing polymorphism