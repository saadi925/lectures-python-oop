'''
Lecture 16: Template Method Pattern

The Template Method Pattern is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure. It promotes reusability and is often used in frameworks.
'''

from abc import ABC, abstractmethod

# Define an abstract class with a template method
class AbstractClass(ABC):
    def template_method(self):
        self.step1()
        self.step2()

    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

# Create concrete subclasses that implement specific steps
class ConcreteClassA(AbstractClass):
    def step1(self):
        print("ConcreteClassA: Step 1")

    def step2(self):
        print("ConcreteClassA: Step 2")

class ConcreteClassB(AbstractClass):
    def step1(self):
        print("ConcreteClassB: Step 1")

    def step2(self):
        print("ConcreteClassB: Step 2")

# Use the Template Method Pattern
class_a = ConcreteClassA()
class_b = ConcreteClassB()

class_a.template_method()
class_b.template_method()

'''
In this example, we have an abstract class AbstractClass with a template method. Concrete subclasses (ConcreteClassA and ConcreteClassB) implement specific steps (step1 and step2). The template method defines the overall algorithm structure and sequence, while the concrete subclasses provide their implementations of individual steps.

Key Points:

The Template Method Pattern defines a common algorithm structure in a superclass but allows specific steps to be overridden in subclasses.
It promotes code reusability by providing a consistent algorithm framework.
It's often used in frameworks and libraries to define the overall flow of an operation while allowing customization at specific points.
'''