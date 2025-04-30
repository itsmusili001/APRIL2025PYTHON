# the __init__ method is a special method that is called when an object is created
#the self parameter is a reference to the current instance of the class
# it allows you to access the attributes and methods of the class in python
class Rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w
    
    
    def calArea(self):
        return self.length * self.width
    def calPerimeter(self):
        return 2 * (self.length + self.width)
    