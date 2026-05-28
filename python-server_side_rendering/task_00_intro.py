#!/usr/bin/python3
"""Introductory task for server-side rendering project.

This module provides a robust function to generate personalized text
invitations from a base template and a list of attendee data.
"""
from typing import Any, Dict, List


def generate_invitations(template: str, attendees: List[Dict[str, Any]]) -> None:
    """Generate personalized invitation files from a template and attendee list.

    Args:
        template (str): The base string containing formatting placeholders.
        attendees (List[Dict[str, Any]]): A list of dictionaries containing
            attendee details.
    """
    # Validate input data types
    if not isinstance(template, str):
        print("Error: Invalid input type for template. Expected str.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(a, dict) for a in attendees
    ):
        print("Error: Invalid input type for attendees. Expected list of dicts.")
        return

    # Check for empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process placeholders and write sequential files
    keys = ["name", "event_title", "event_date", "event_location"]

    for idx, attendee in enumerate(attendees, start=1):
        content = template

        for key in keys:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace(f"{{{key}}}", str(value))

        filename = f"output_{idx}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
        except IOError as e:
            print(f"Error: Could not write to {filename}. Details: {e}")

