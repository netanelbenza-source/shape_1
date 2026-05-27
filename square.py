from shape import Shape

class Square(Shape):

    def __init__(self,side):
            
            self.side = side
           
            def get_area(self):
                return self.side * self.side
            
            def get_perimeter(self):
                return self.side * 4
            
            def get_repr(self):
                return f":width{self.width},height:{self.height}"