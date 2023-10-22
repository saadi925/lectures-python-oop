'''
Lecture 6: Aggregation in Object-Oriented Programming

Aggregation is a form of association between objects in Object-Oriented Programming (OOP). It represents a "has-a" relationship, where one class contains or owns objects of another class, but the contained objects can exist independently of the container. Aggregation is often used to model parts-whole relationships.
'''
class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create instances of Author and Book using aggregation
author = Author("J.K. Rowling")
book = Book("Harry Potter and the Sorcerer's Stone", author) # here book is container

# Access book information, including the author
print(f"Book Title: {book.title}")
print(f"Author: {book.author.name}")

'''
In this example, we have two classes, Author and Book. The Book class contains an instance of the Author class, demonstrating an aggregation relationship. The Book "has" an author, but the author can exist independently of the book.

Key Points:

Aggregation is used to model a part-whole relationship where one class (the container) contains objects of another class (the contained objects).
The contained objects in an aggregation can exist independently and may be shared among multiple containers.
Aggregation is a more flexible form of association compared to composition, as the contained objects can be reused in different contexts.
'''