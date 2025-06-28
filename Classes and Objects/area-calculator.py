class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
r1=Rectangle(10,5)
r2=Rectangle(10,12)
print(f"Area of Rectangle 1 : {r1.area()}")
print(f"Area of Rectangle 2 is :{r2.area()}")
print(f"Perimeter of Rectangle 1 : {r1.perimeter()}")
print(f"Perimeter of Rectangle 2 :{r2.perimeter()}")