'''
Lecture 12: Decorator Pattern

The Decorator Pattern is a structural design pattern that allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class. It is used to extend the functionality of classes in a flexible and reusable way.
'''

# Define a base component interface
class Coffee:
    def cost(self):
        pass

# Create a concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5  # Base price of simple coffee

# Define a decorator class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Create concrete decorator classes
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2  # Add the cost of milk

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1  # Add the cost of sugar

# Use the Decorator Pattern
coffee = SimpleCoffee()
print(f"Cost of Simple Coffee: ${coffee.cost()}")

coffee_with_milk = MilkDecorator(coffee)
print(f"Cost of Coffee with Milk: ${coffee_with_milk.cost()}")

coffee_with_sugar = SugarDecorator(coffee)
print(f"Cost of Coffee with Sugar: ${coffee_with_sugar.cost()}")

coffee_with_milk_and_sugar = SugarDecorator(MilkDecorator(coffee))
print(f"Cost of Coffee with Milk and Sugar: ${coffee_with_milk_and_sugar.cost()}")

'''
In this example, we have a base component class Coffee and a concrete component class SimpleCoffee. Decorators, such as MilkDecorator and SugarDecorator, extend the behavior of the component by adding the cost of milk and sugar. Decorators can be stacked to create complex combinations of behavior.

Key Points:

The Decorator Pattern allows you to add behavior to objects dynamically without changing their code.
It's a flexible alternative to subclassing for extending functionality.
Decorators can be combined and stacked to create complex combinations of behavior.
'''