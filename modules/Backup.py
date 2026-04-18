# modules/backup.py
import os
import shutil
from datetime import datetime
from modules.logger import log

def backup_files(source, destination, log_file):

    if not os.path.exists(destination):
        os.makedirs(destination)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder = os.path.join(destination, f"backup_{timestamp}")

    os.makedirs(backup_folder)

    for file in os.listdir(source):
        src_path = os.path.join(source, file)

        if os.path.isfile(src_path):
            try:
                shutil.copy2(src_path, backup_folder)
                log(f"FILE COPIED: {file}", log_file)

            except Exception as e:
                log(f"ERROR copying {file}: {e}", log_file)

    return backup_folder
