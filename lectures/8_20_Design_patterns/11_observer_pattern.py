'''
Lecture 11: Observer Pattern

The Observer Pattern is a behavioral design pattern that defines a one-to-many dependency between objects, so when one object (the subject) changes state, all its dependents (observers) are notified and updated automatically. It is used to create distributed and event-driven systems.
'''

from abc import ABC, abstractmethod

# Define an abstract subject class
class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def set_state(self, state):
        pass

# Define an abstract observer class
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

# Create concrete subject and observer classes
class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state
        self.notify()

class ConcreteObserver(Observer):
    def __init__(self, name, subject):
        self._name = name
        self._subject = subject

    def update(self):
        state = self._subject.get_state()
        print(f"Observer {self._name} received update with state: {state}")

# Use the Observer Pattern
subject = ConcreteSubject()
observer1 = ConcreteObserver("Observer 1", subject)
observer2 = ConcreteObserver("Observer 2", subject)

subject.attach(observer1)
subject.attach(observer2)

subject.set_state("New State")

'''
In this example, the Subject class maintains a list of observers and notifies them when its state changes. Observers, represented by the Observer class, can be attached to the subject. When the subject's state changes, it notifies all attached observers, who then update themselves based on the new state.

Key Points:

The Observer Pattern establishes a one-to-many relationship between a subject and its observers.
Observers are notified and updated automatically when the subject's state changes.
It's useful for building distributed and event-driven systems, where multiple parts of a system need to respond to state changes.
If you have any questions about the Observer Pattern or would like to explore another design pattern or topic, please let me know!
'''