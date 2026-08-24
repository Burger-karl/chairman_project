from datetime import datetime
from money_book.diary import log_event


def add_member(records):
    name = input("Member's name: ").strip()

    if name in records:
        print(name + " is already a number.")
        return

    records[name] = {
        "joined": datetime.now().strftime("%Y-%m-%d"),
        "payments": []
    }

    print("Added new member: " + name)
    log_event("Added new member: " + name)


def list_members(records):
    if not records:
        print("No members yet")
        return

    print("\n==== Members ====")
    for name in records:
        print(name)
