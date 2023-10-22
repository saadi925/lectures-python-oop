'''
Lecture 18: Composite Pattern

The Composite Pattern is a structural design pattern that lets you compose objects into tree structures to represent part-whole hierarchies. It allows clients to treat individual objects and compositions of objects uniformly.
'''
from abc import ABC, abstractmethod

# Define a common component interface
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# Create leaf components
class Leaf(Component):
    def operation(self):
        return "Leaf"

# Create composite components
class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Composite: {', '.join(results)}"

# Use the Composite Pattern
leaf1 = Leaf()
leaf2 = Leaf()
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)

result = composite.operation()
print(result)

'''
In this example, we have a common interface Component that's implemented by both leaf components (Leaf) and composite components (Composite). The composite component can hold a collection of child components and treats them uniformly. The composite component's operation method aggregates the results of its child components.

Key Points:

The Composite Pattern allows you to create part-whole hierarchies of objects.
It lets clients treat individual objects and compositions of objects uniformly.
It's useful for building complex structures that can be treated as a single unit.
'''