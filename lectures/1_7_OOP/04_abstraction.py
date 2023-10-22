'''
Lecture 4: Abstraction in Object-Oriented Programming

Abstraction is one of the key principles of Object-Oriented Programming (OOP) and is related to encapsulation. Abstraction focuses on the idea of simplifying complex reality by modeling classes based on real-world objects and their essential characteristics. It involves showing only necessary features of an object while hiding the unnecessary details.
'''
from abc import ABC, abstractmethod

# Create an abstract base class using ABC (Abstract Base Class)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Create concrete subclasses that inherit from Shape
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

# Create instances of Rectangle and Circle
rect = Rectangle(5, 4)
circle = Circle(3)

# Calculate and print the areas of shapes
print(f"Area of Rectangle: {rect.area()}")
print(f"Area of Circle: {circle.area()}")


'''
In this example, we use an abstract base class Shape to define a common interface for any shape, forcing its subclasses to implement the area method. The concrete subclasses, Rectangle and Circle, provide their implementations of the area method, which abstracts away the details of how the area is calculated.

Key Points:

Abstraction is about simplifying complex systems by modeling classes and objects based on their essential characteristics and behaviors.
Abstract classes, like the Shape class in the example, define a common interface (method signatures) that must be implemented by concrete subclasses.
Abstraction helps in managing complexity, promoting code reusability, and making your code more maintainable.
If you have any questions or want to explore another OOP concept, please feel free to ask!
'''

# Why we are using @abstactmethod and ABC  
'''
The ABC (Abstract Base Class) module in Python is used to define abstract base classes, which are classes that are meant to be subclassed by other classes. Abstract base classes provide a way to define a common interface for a set of related classes. The @abstractmethod decorator is used in combination with ABC to mark methods as abstract, indicating that any concrete subclass must implement these methods.

Here's why we use ABC and the @abstractmethod decorator:

Defining Abstract Base Classes (ABCs): In Python, abstract base classes are a way to define a common interface or set of methods that multiple related classes should implement. They serve as a form of contract, ensuring that any concrete subclass adheres to the specified interface. This can help make your code more maintainable and predictable.

@abstractmethod Decorator: When you mark a method with the @abstractmethod decorator, you're declaring that it's meant to be an abstract method. An abstract method is a method that is declared in the abstract base class but doesn't provide an implementation. Concrete subclasses are required to provide their own implementation for abstract methods.

By using @abstractmethod, you're essentially telling Python that any subclass that doesn't implement the abstract method should be considered incomplete and can't be instantiated.
Here's why these tools are necessary:

Contract and Interface Enforcement: Abstract base classes and abstract methods enforce a contract between the base class and its subclasses. They ensure that specific methods are implemented in concrete subclasses, promoting a consistent and predictable interface.

Run-Time Error Prevention: Using abstract methods helps prevent run-time errors where you might accidentally forget to implement a required method in a subclass.

Documentation and Guidance: Abstract base classes also serve as a form of documentation, indicating the expected behavior for subclasses.

In the previous example, we used ABC and @abstractmethod to create the Shape abstract base class, defining an interface that any shape class should adhere to. Concrete subclasses like Rectangle and Circle were then forced to implement the area method, ensuring that they provide the necessary functionality.


 ABC and the @abstractmethod decorator are essential tools for defining abstract base classes and specifying abstract methods, ensuring that subclasses adhere to a common interface and providing clear guidelines for method implementation.
'''