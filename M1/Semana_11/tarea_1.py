class Circle:
    def __init__(self,radius):
        self.radius = radius
    def get_area(self):
        pi = 3.14
        print(f"el area es {(self.radius**2)* pi}")


robin = Circle(1)
robin.get_area()        
