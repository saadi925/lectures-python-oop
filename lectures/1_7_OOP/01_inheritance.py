'''
Lecture 1: Inheritance in Object-Oriented Programming

Inheritance is a fundamental concept in OOP that allows you to create a new class (subclass or derived class) by inheriting properties and behaviors from an existing class (base class or parent class). It promotes code reusability and the organization of classes in a hierarchical structure.


In this example, we have a base class Animal with a common attribute name and an abstract method speak. The Dog class is a subclass of Animal and overrides the speak method to provide its own implementation.
'''
# Define a base class (parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Define a subclass (child class) that inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Create instances of the classes
cat = Animal("Whiskers")
dog = Dog("Buddy")

# Call the speak method on both instances
print(cat.speak())  # This will raise a NotImplementedError in the parent class
print(dog.speak())  # This will execute the speak method in the Dog class


'''


Key Points:

Inheritance allows a subclass to inherit attributes and methods from a parent class.
The super() function is used to access the methods and attributes of the parent class from within the child class.
You can override methods in the child class to provide specialized behavior.
Now, let's move on to the next OOP concept or any questions you might have about inheritance.
'''