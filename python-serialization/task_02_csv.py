#!/usr/bin/env python3
"""Convert CSV data to JSON."""

import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON and save it as data.json."""
    try:
        with open(filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
