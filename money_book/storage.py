import json
import os

DATA_FILE = os.path.join("data", "records.json")

def load_records():
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Saved records look damaged. Starting fresh.")
        os.rename(DATA_FILE, DATA_FILE + ".corrupted")
        return {}

def save_records(records):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(records, f, indent=4)