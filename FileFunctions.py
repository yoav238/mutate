import csv
import os
import shutil
from pathlib import Path
import os

def list_files_in_folder(folder_path):
    """
    Returns a list of all file names in the given folder.

    Parameters:
    folder_path (str): The path to the folder.

    Returns:
    List[str]: A list of file names in the folder.
    """
    try:
        # List all files in the folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        return files
    except Exception as e:
        print(f"Error: {e}")
        return []

def move_latest_file(source_folder, destination_folder):
    """
    Move the latest created file from the source folder to the destination folder.

    Parameters:
    source_folder (str): The path of the source folder.
    destination_folder (str): The path of the destination folder.

    Returns:
    None
    """
    try:
        # Ensure the destination folder exists
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Get all files in the source folder
        files = [f for f in Path(source_folder).iterdir() if f.is_file()]

        # Check if there are any files in the source folder
        if not files:
            print("No files found in the source folder.")
            return

        # Find the latest created file
        latest_file = max(files, key=lambda f: f.stat().st_ctime)

        # Create the target file path
        target_path = os.path.join(destination_folder, latest_file.name)

        # Move the file to the target folder
        shutil.move(str(latest_file), target_path)

        print(f"File moved to {target_path}")
    except Exception as e:
        print(f"Error: {e}")


def move_file(file_path, folder_path):
    """
    Move a file from its original location to a new folder.

    Parameters:
    file_path (str): The path of the file to be moved.
    folder_path (str): The path of the folder to move the file to.

    Returns:
    None
    """
    try:
        # Ensure the target folder exists
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Get the file name from the file path
        file_name = os.path.basename(file_path)

        # Create the target file path
        target_path = os.path.join(folder_path, file_name)

        # Move the file to the target folder
        shutil.move(file_path, target_path)

        print(f"File moved to {target_path}")
    except Exception as e:
        print(f"Error: {e}")

def read_csv_to_string_array(file_path):
    """
    Reads a CSV file and returns a list of all values as strings.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    List[str]: A list of all values in the CSV file as strings.
    """
    values = []

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                for value in row:
                    values.append(value)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")

    return values


def read_csv_to_double_array(file_path):

    double_array = []

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8-sig') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if len(row) >= 2:  # Ensure there are at least two columns
                    double_array.append([row[0], row[1]])  # Append columns A and B
    except Exception as e:
        print(f"Error reading the CSV file: {e}")

    return double_array