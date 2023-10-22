'''
Lecture 2: Polymorphism in Object-Oriented Programming

Polymorphism is a core OOP concept that allows objects of different classes to be treated as objects of a common superclass. It enables you to write code that can work with objects of multiple classes in a unified way.
'''

# Create a base class
class Shape:
    def area(self):
        pass

# Create two subclasses of Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

# Create a function that calculates the area of any shape
def calculate_area(shape):
    return shape.area()

# Create instances of Rectangle and Circle
rect = Rectangle(5, 4)
circle = Circle(3)

# Use the calculate_area function with different shapes
print(f"Area of Rectangle: {calculate_area(rect)}")
print(f"Area of Circle: {calculate_area(circle)}")



'''
In this example, we have a base class Shape with an abstract method area. We then create two subclasses, Rectangle and Circle, both of which override the area method to provide their specific implementations. The calculate_area function can accept any shape (object of a class that inherits from Shape) and calculate its area.

Key Points:

Polymorphism allows you to treat different objects as instances of a common superclass, simplifying code that works with a variety of objects.
In Python, polymorphism is achieved through method overriding, where different classes provide their own implementation of methods defined in a common superclass.
'''