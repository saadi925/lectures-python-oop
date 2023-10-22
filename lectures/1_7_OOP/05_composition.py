'''
Lecture 5: Composition in Object-Oriented Programming

Composition is a design principle in Object-Oriented Programming (OOP) that promotes building complex objects by combining simpler objects. Instead of relying on inheritance, composition allows you to create more flexible and modular systems by assembling objects with distinct responsibilities.
'''

# Create two classes that represent parts of a computer
class CPU:
    def process(self):
        print("Processing data")

class RAM:
    def store(self):
        print("Storing data")

# Create a Computer class that uses composition to combine CPU and RAM
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()

    def perform_task(self):
        print("Computer is performing a task...")
        self.cpu.process()
        self.ram.store()

# Create an instance of the Computer class
my_computer = Computer()

# Use composition to perform a task
my_computer.perform_task()


'''
In this example, we have two classes, CPU and RAM, which represent parts of a computer. The Computer class uses composition to combine these parts by creating instances of CPU and RAM as attributes. The perform_task method of the Computer class uses the functionality provided by the CPU and RAM objects.

Key Points:

Composition promotes flexibility and modularity by allowing you to build complex objects by assembling simpler objects.
Instead of inheriting behaviors from other classes, composition involves creating instances of other classes as attributes and delegating functionality to them.
'''