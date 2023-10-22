'''
Lecture 20: State Pattern

The State Pattern is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. The object will appear to change its class. It's used to represent the state of an object and its transitions.
'''
from abc import ABC, abstractmethod

# Define an abstract state interface
class State(ABC):
    @abstractmethod
    def handle(self):
        pass

# Create concrete state classes
class StateA(State):
    def handle(self):
        return "State A behavior"

class StateB(State):
    def handle(self):
        return "State B behavior"

# Create a context class that can change its state
class Context:
    def __init__(self, state):
        self._state = state

    def request(self):
        return self._state.handle()

    def change_state(self, new_state):
        self._state = new_state

# Use the State Pattern
state_a = StateA()
state_b = StateB()

context = Context(state_a)
result1 = context.request()
print(result1)

context.change_state(state_b)
result2 = context.request()
print(result2)
'''
In this example, we have an abstract state class State with concrete state classes StateA and StateB. The Context class can change its state, and when it requests behavior, it delegates to the current state. Changing the state of the context changes its behavior.

Key Points:

The State Pattern allows an object to change its behavior when its internal state changes.
It represents the state and transitions of an object.
It's useful for managing complex state-dependent behaviors.
'''


# Do you have to learn all the design patterns 

'''
That said, it's not necessary to memorize all design patterns or try to fit them into every project. Instead, focus on understanding the principles and concepts behind design patterns. When you encounter a problem that aligns with a specific pattern, you can then apply it or modify it to suit your needs. Design patterns are tools in a developer's toolbox, and you should use them when they are the right fit for a particular situation.

Start with the most commonly used design patterns, such as the Singleton, Factory Method, Observer, Decorator, and Strategy patterns. As you gain experience, you can explore more patterns and deepen your understanding of software design.
'''