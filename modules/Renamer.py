# modules/renamer.py
import os
from modules.logger import log

def rename_files(folder, log_file):

    count = 1

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            ext = file.split(".")[-1]
            new_name = f"file_{count}.{ext}"

            new_path = os.path.join(folder, new_name)

            try:
                os.rename(path, new_path)
                log(f"RENAMED {file} -> {new_name}", log_file)
                count += 1

            except Exception as e:
                log(f"ERROR renaming {file}: {e}", log_file)
