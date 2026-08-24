import os
from datetime import datetime

LOG_FILE = os.path.join("data", "dairy.log")

def log_event(message):
    os.makedirs("data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as f:
        f.write(timestamp + " - " + message + "\n")

