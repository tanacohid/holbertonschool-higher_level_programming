#!/usr/bin/python3
"""
Task 0: Creating a Simple Templating Program
"""


class SafeDict(dict):
    """Custom dictionary to handle missing keys or None values with 'N/A'."""
    def __getitem__(self, key):
        try:
            val = super().__getitem__(key)
            if val is None:
                return "N/A"
            return val
        except KeyError:
            return "N/A"


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.
    """
    # Verify that template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Verify that attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(
        isinstance(item, dict) for item in attendees
    ):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if the template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check if the attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Iterate over attendees and generate output files sequentially
    for index, attendee in enumerate(attendees, start=1):
        safe_attendee = SafeDict(attendee)

        # Replace placeholders in the template
        try:
            content = template.format_map(safe_attendee)
        except Exception:
            content = template

        # Write to output_X.txt
        filename = f"output_{index}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
