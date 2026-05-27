from shape import Shape
import math

class Circle(Shape):
    def __init__(self,radius):
        
        self.radius = radius
        
        def get_area(self):
            return math.pi *  math.pow(self.radius,2)

            
        def get_perimeter(self):
            return 2 * math.pi * self.radius
        
        
        def get_repr(self):
         return f"radius:{self.radius}"
