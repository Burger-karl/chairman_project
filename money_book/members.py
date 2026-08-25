from datetime import datetime
import os
from money_book.diary import log_event


def add_member(records):
    name = input("Member's name: ").strip()

    if name in records:
        print(name + " is already a member.")
        return

    records[name] = {
        "joined": datetime.now().strftime("%Y-%m-%d"),
        "payments": []
    }

    print("Added new member: " + name)
    log_event("Added new member: " + name)


def list_members(records):
    if not records:
        print("No members yet.")
        return

    print("\n--- Members ---")
    for name in records:
        print(name)


def import_members_from_file(records, filepath="new_members.txt"):
    if not os.path.exists(filepath):
        print("File not found: " + filepath)
        return

    with open(filepath, "r") as f:
        lines = f.readlines()

    added = 0
    skipped = 0

    for line in lines:
        name = line.strip()

        if not name:
            skipped += 1
            continue

        if not name.replace(" ", "").isalpha():
            print("Skipping invalid line: " + repr(line.strip()))
            skipped += 1
            continue

        if name in records:
            print(name + " is already a member. Skipping.")
            skipped += 1
            continue

        records[name] = {
            "joined": datetime.now().strftime("%Y-%m-%d"),
            "payments": []
        }
        added += 1
        log_event("Imported new member: " + name)

    print("Import complete. Added " + str(added) + ", skipped " + str(skipped) + ".")