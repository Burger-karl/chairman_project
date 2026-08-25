import json
import os
import shutil
from datetime import datetime

DATA_FILE = os.path.join("data", "records.json")


def load_records():
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Saved records look damaged. Starting fresh.")
        return {}


def save_records(records):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(records, f, indent=4)


def backup_records():
    if not os.path.exists(DATA_FILE):
        print("No records to back up yet.")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    backup_file = os.path.join("data", "records_backup_" + today + ".json")
    shutil.copy(DATA_FILE, backup_file)
    print("Backup saved as " + backup_file)