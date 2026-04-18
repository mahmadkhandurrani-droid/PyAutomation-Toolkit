import json
from modules.backup import backup_files
from modules.organizer import organize_folder
from modules.renamer import rename_files
from modules.reporter import generate_report

with open("config.json", "r") as f:
    config = json.load(f)

source = config["source_folder"]
backup = config["backup_folder"]
log_file = config["log_file"]
report_file = config["report_file"]

while True:

    print("\n=== PAT MENU ===")
    print("1. Backup Files")
    print("2. Organize Folder")
    print("3. Rename Files")
    print("4. Generate Report")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        backup_files(source, backup, log_file)

    elif choice == "2":
        organize_folder(source, log_file)

    elif choice == "3":
        rename_files(source, log_file)

    elif choice == "4":
        generate_report(log_file, report_file)

    elif choice == "5":
        break

    else:
        print("Invalid choice")
