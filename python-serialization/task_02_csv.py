#!/usr/bin/env python3
"""CSV serialization"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file to JSON format and saves it to data.json.

    Args:
        csv_filename: The name of the CSV file to convert.

    Returns:
        True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
