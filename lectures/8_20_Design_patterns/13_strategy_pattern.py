'''
Lecture 13: Strategy Pattern

The Strategy Pattern is a behavioral design pattern that defines a family of algorithms, encapsulates each one, and makes them interchangeable. It allows clients to choose the appropriate algorithm at runtime, providing flexibility and promoting code reuse.
'''
from abc import ABC, abstractmethod

# Define an abstract strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Create concrete strategy classes
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} with a credit card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} with PayPal")

# Create a context that uses the strategy
class ShoppingCart:
    def __init__(self, payment_strategy):
        self._items = {}
        self._payment_strategy = payment_strategy

    def add_item(self, item, price):
        self._items[item] = price

    def calculate_total(self):
        return sum(self._items.values())

    def checkout(self):
        total = self.calculate_total()
        self._payment_strategy.pay(total)

# Use the Strategy Pattern
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

cart = ShoppingCart(credit_card_payment)
cart.add_item("Item 1", 30)
cart.add_item("Item 2", 20)
cart.checkout()

cart = ShoppingCart(paypal_payment)
cart.add_item("Item 3", 15)
cart.checkout()

'''
In this example, we have an abstract PaymentStrategy interface and concrete strategy classes (CreditCardPayment and PayPalPayment). The ShoppingCart class uses a payment strategy to calculate the total and process the payment. Different payment strategies can be swapped at runtime, making the code flexible and easy to extend.

Key Points:

The Strategy Pattern defines a family of algorithms, encapsulates each one, and allows them to be interchangeable.
It promotes flexibility and reusability by separating algorithms from the client code.
Clients can choose the appropriate strategy at runtime.
'''