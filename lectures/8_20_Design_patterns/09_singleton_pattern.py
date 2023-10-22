'''
Lecture 9: Singleton Pattern

The Singleton Pattern is a design pattern that restricts a class from instantiating multiple objects and ensures that it has only one instance. This pattern is used when exactly one object is needed to coordinate actions across the system.
'''

class Singleton:
    _instance = None  # Class variable to store the single instance

    def __new__(cls): # control the object creation process (new method)
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = 0  # Initialize some attribute
        return cls._instance

# Creating instances
singleton1 = Singleton()
singleton1.value = 10
singleton2 = Singleton()

# Both instances are the same
print(singleton1 is singleton2)  # Output: True

# Values are shared
print(singleton2.value)  # Output: 0 (from singleton2)

'''
In this example, the Singleton class ensures that only one instance is created. The __new__ method is used to control the object creation process. When you create an instance of the Singleton class, it checks if an instance already exists. If it does, it returns the existing instance; otherwise, it creates a new one.

Key Points:

The Singleton Pattern ensures that a class has only one instance and provides a global point of access to that instance.
It's often used to control access to resources, such as a database connection or a logging service, where having multiple instances would be problematic.
In Python, you can implement the Singleton Pattern by overriding the __new__ method and using a class variable to store the single instance.
'''


# why super() here ?

'''
In the Singleton Pattern implementation in Python, using super is not strictly necessary, and you can create the instance without it. The use of super in that context is a common pattern, but it doesn't affect the behavior of the Singleton Pattern itself. Let me clarify its purpose and usage.

The super function is typically used in Python to call a method in a superclass or superclass's superclass. It allows you to call a method from a parent class when you've overridden that method in a subclass. In the context of the Singleton Pattern, the super function is used to call the __new__ method of the base class (object) to create a new instance of the class. Here's the line in question:
'''
# cls._instance = super(Singleton, cls).__new__(cls)
'''
super(Singleton, cls) sets up the call to the __new__ method of the object class (the base class). The super function is used to access the superclass, in this case, object.

__new__(cls) is called to create a new instance of the class (cls).

The new instance is assigned to cls._instance, which is used to store the single instance of the class.

While the use of super is a common practice to ensure that the __new__ method is called from the base class, you can also call object.__new__(cls) directly without using super in this specific context. The goal is to create a new instance of the class without creating multiple instances, ensuring that the Singleton pattern is upheld.
'''
# cls._instance = object.__new__(cls)
'''
This line achieves the same result as the previous one. The use of super is a matter of coding style and personal preference, but it doesn't change the fundamental behavior of the Singleton Pattern in this context.
'''
