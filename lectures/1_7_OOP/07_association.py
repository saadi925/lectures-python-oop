'''
Lecture 7: Association in Object-Oriented Programming

Association is a fundamental concept in OOP that describes how objects interact with each other. It represents a "using" or "interacting" relationship between objects. Unlike composition and aggregation, association doesn't imply ownership or containment; it simply means that two classes are related in some way.
'''
class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name):
        self.name = name

class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course

# Create instances of Student and Course
alice = Student("Alice")
math_course = Course("Mathematics")

# Create an Enrollment to associate Student and Course
enrollment = Enrollment(alice, math_course)

# Access information about the association
print(f"{enrollment.student.name} is enrolled in {enrollment.course.name}")

'''
In this example, we have three classes: Student, Course, and Enrollment. The Enrollment class represents an association between a student and a course, but it doesn't imply ownership or containment. Students and courses can exist independently, and multiple students can be associated with the same course.

Key Points:

Association represents the relationship between objects where one object interacts with another.
Unlike composition and aggregation, association doesn't imply ownership or containment; it represents a looser, more general relationship.
Associations are often used to model relationships between objects in a system.
'''

# it resembles aggregation ?
'''
You're correct; the example might resemble aggregation, and it's important to highlight the subtle differences between the two concepts. Both aggregation and association represent relationships between objects, but the key distinction is the degree of ownership or containment.

In an aggregation relationship, the contained objects can exist independently and may be shared among multiple containers. The relationship often implies a "has-a" or "part-of" relationship, where the container can exist without the contained objects, and the contained objects are typically shared among multiple containers.

In an association relationship, the objects are related but don't necessarily imply ownership or containment. It's a more general "uses" or "interacts" relationship, where the objects involved can exist independently, and the association might be more dynamic.

In the example I provided, the Enrollment class could be seen as an aggregation relationship, but it can also be interpreted as an association if you consider that the student and the course can exist independently, and the relationship is more about interaction. The distinction can sometimes be subtle and context-dependent.

So, you are right to notice the similarity, and it's important to remember that the choice between association and aggregation depends on the specific modeling needs and the relationships you want to represent in your system.
'''