'''
Lecture 14: Command Pattern

The Command Pattern is a behavioral design pattern that turns a request into a stand-alone object, allowing you to parameterize clients with requests, queue or log requests, and support undoable operations. It decouples the sender and receiver of a request.
'''
from abc import ABC, abstractmethod

# Define a command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Create concrete command classes
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Create receiver classes
class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")

# Create invoker class
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Use the Command Pattern
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote_control = RemoteControl()
remote_control.set_command(light_on)
remote_control.press_button()

remote_control.set_command(light_off)
remote_control.press_button()
'''
In this example, we have a Command interface with concrete command classes (LightOnCommand and LightOffCommand). The Light class acts as the receiver, which performs the actual actions. The RemoteControl class is the invoker that sets and executes commands.

Key Points:

The Command Pattern encapsulates a request as an object, decoupling the sender and receiver of the request.
It allows you to parameterize objects with operations, queue requests, log them, or support undoable operations.
It's useful in scenarios where you need to support a variety of actions or operations and need to keep the sender and receiver decoupled.
'''