import csv
import os

def load_csv_data(file_path):
    """Reads a CSV file into a list of dictionaries"""
    if os.path.exists(file_path):
        data_list = []
        with open(file_path, mode="r", encoding="utf-8") as fhand:
            csv_reader = csv.DictReader(fhand)
            for row in csv_reader:
                data_list.append(row)
        return data_list
    else:
        print(f"Warning: The file {file_path} was not found.")
        return []