class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length  # If width is not provided, it's a square

    def area(self):
        return self.length * self.width

# Demonstration
square = Rectangle(5)
rectangle = Rectangle(5, 10)
print("Square Area:", square.area())
print("Rectangle Area:", rectangle.area())
