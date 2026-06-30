class Shape:
    def area(self):
        print("Area calculation")
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        super().area()
        return (3.14*self.r*self.r)
class Triangle(Shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def area(self):
        super().area()
        return (self.b*self.h)/2
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        super().area()
        return self.l*self.b
class Square(Shape):
    def __init__(self,a):
        self.a=a
    def area(self):
        super().area()
        return self.a**2
circle=Circle(10)
triangle=Triangle(2,4)
rectangle=Rectangle(5,2)
square=Square(4)
shapes=[circle,triangle,rectangle,square]
for shape in shapes:
    print(shape.area())