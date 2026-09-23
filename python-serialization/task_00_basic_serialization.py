#!/usr/bin/env python3
"""Basic serialization and deserialization."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary and save it to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load a JSON file and return the deserialized dictionary."""
    with open(filename, "r") as file:
        return json.load(file)
