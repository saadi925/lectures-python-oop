'''
Lecture 3: Encapsulation in Object-Oriented Programming

Encapsulation is one of the four fundamental OOP concepts and is often described as the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, called a class. It's about hiding the internal details of how a class works and exposing only the necessary parts to the outside world. In Python, encapsulation can be achieved using private and protected attributes.
'''

class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Protected attribute

    def display(self):
        print(f"Name: {self.name}, Age: {self._age}")

    # Private method
    def _study(self, subject):
        print(f"{self.name} is studying {subject}")

    # Public method
    def study_subject(self, subject):
        self._study(subject)

# Create an instance of the Student class
student1 = Student("Alice", 20)

# Access and display attributes
student1.display()

# Try to access a protected attribute (not recommended)
print(student1._age)  # This is allowed but not recommended

# Try to call a private method (not recommended)
student1._study("Math")  # This is allowed but not recommended

# Call a public method to study a subject
student1.study_subject("History")

'''
In this example, we have a Student class with a public attribute name, a protected attribute _age, a private method _study, and a public method study_subject. Encapsulation is achieved by using an underscore prefix for the protected and private attributes/methods.

Key Points:

Encapsulation helps in data hiding and maintaining the integrity of data by controlling access to attributes and methods.
Public attributes and methods can be accessed from outside the class. Protected attributes and methods are accessible but not recommended for external use. Private attributes and methods are not meant to be accessed from outside the class.
'''