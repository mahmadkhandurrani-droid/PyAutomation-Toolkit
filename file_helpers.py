# utils/file_helpers.py
import os

def get_all_files(folder):
    files = []
    for item in os.listdir(folder):
        full_path = os.path.join(folder, item)
        if os.path.isfile(full_path):
            files.append(full_path)
    return files
