# modules/reporter.py

def generate_report(log_file, report_file):

    with open(log_file, "r") as f:
        logs = f.readlines()

    total = len(logs)

    with open(report_file, "w") as f:
        f.write("=== AUTOMATION REPORT ===\n")
        f.write(f"Total operations logged: {total}\n")

    print("Report generated.")
