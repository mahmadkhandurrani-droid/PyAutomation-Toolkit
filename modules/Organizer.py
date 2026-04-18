# modules/organizer.py
import os
import shutil
from modules.logger import log

def organize_folder(folder, log_file):

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            ext = file.split(".")[-1]

            target_folder = os.path.join(folder, ext.upper())

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            try:
                shutil.move(path, target_folder)
                log(f"MOVED {file} -> {ext.upper()}", log_file)

            except Exception as e:
                log(f"ERROR moving {file}: {e}", log_file)
