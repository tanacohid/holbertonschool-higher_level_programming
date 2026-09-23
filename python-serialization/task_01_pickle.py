#!/usr/bin/env python3
"""Define a serializable custom Python object."""

import pickle


class CustomObject:
    """Represent a custom object that can be serialized."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current object to a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (OSError, pickle.PickleError, EOFError, AttributeError):
            return None
