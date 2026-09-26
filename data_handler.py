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

def save_csv_data(file_path, data_list):
    """Writes a list of dictionaries back into a CSV file."""
    if len(data_list) == 0:
        return
        
    csv_headers = data_list[0].keys()
    with open(file_path, mode="w", newline="", encoding="utf-8") as fhand:
        csv_writer = csv.DictWriter(fhand, fieldnames=csv_headers)
        csv_writer.writeheader()
        csv_writer.writerows(data_list)