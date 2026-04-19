#!/usr/bin/python3
"""
Module to convert CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads a CSV file and converts its content into a JSON file named data.json.
    Returns True if successful, False otherwise.
    """
    try:
        data = []
        with open(csv_filename, mode='r', encoding='utf-8') as csv_f:
            reader = csv.DictReader(csv_f)
            for row in reader:
                data.append(row)

        with open('data.json', mode='w', encoding='utf-8') as json_f:
            json.dump(data, json_f)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
