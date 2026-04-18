# modules/logger.py
from datetime import datetime

def log(message, log_file):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{time}] {message}\n"

    with open(log_file, "a") as f:
        f.write(full_message)

    print(full_message.strip())
