'''Lecture 10: Factory Method Pattern

The Factory Method Pattern is a creational design pattern that defines an interface for creating an object, but it lets subclasses alter the type of objects that will be created. It provides a way to delegate the responsibility of instantiating objects to its subclasses.'''

from abc import ABC, abstractmethod

# Define an abstract creator class
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def operation(self):
        product = self.factory_method()
        return f"Creator: {product.operation()}"

# Define concrete product classes
class ConcreteProductA:
    def operation(self):
        return "Product A operation."

class ConcreteProductB:
    def operation(self):
        return "Product B operation."

# Create concrete creator classes
class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Use the factory method pattern
creator_a = ConcreteCreatorA()
product_a = creator_a.operation()
print(product_a)

creator_b = ConcreteCreatorB()
product_b = creator_b.operation()
print(product_b)

'''
In this example, we have an abstract Creator class that defines the factory_method. Subclasses of Creator (e.g., ConcreteCreatorA and ConcreteCreatorB) implement the factory method to create specific product objects (e.g., ConcreteProductA and ConcreteProductB). The Creator class's operation method delegates object creation to the factory method and operates on the product.

Key Points:

The Factory Method Pattern defines an interface for creating objects but lets subclasses decide which class to instantiate.
It promotes loose coupling by allowing a class to delegate the responsibility of instantiating objects to its subclasses.
It's useful when a class cannot anticipate the class of objects it needs to create.
'''