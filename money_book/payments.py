from datetime import datetime
from money_book.diary import log_event


def record_payment(records):
    name = input("Member's name: ").strip()

    if name not in records:
        print(name + " is not a registered member.")
        return

    month = None
    while month is None:
        month_input = input("Which month is this payment for? (e.g. August 2026): ").strip()
        try:
            parsed = datetime.strptime(month_input, "%B %Y")
            month = parsed.strftime("%B %Y")
        except ValueError:
            print("Please enter the month exactly like this: August 2026")

    amount = float(input("Amount paid: "))
    date_paid = datetime.now().strftime("%Y-%m-%d")

    payment = {
        "month": month,
        "amount": amount,
        "date_paid": date_paid
    }
    records[name]["payments"].append(payment)

    print("Recorded payment of " + str(amount) + " from " + name + " for " + month + ".")
    log_event(name + " paid " + str(amount) + " for " + month)


def show_owe_status(records):
    if not records:
        print("No members yet.")
        return

    current_year = datetime.now().year
    current_month_num = datetime.now().month

    # Build every month from January up to the current month, e.g.
    # ["January 2026", "February 2026", ..., "August 2026"]
    expected_months = []
    for month_num in range(1, current_month_num + 1):
        month_name = datetime(current_year, month_num, 1).strftime("%B %Y")
        expected_months.append(month_name)

    paid = []
    owing = []

    for name in records:
        paid_months = []
        for payment in records[name]["payments"]:
            paid_months.append(payment["month"])

        missing_months = []
        for month in expected_months:
            if month not in paid_months:
                missing_months.append(month)

        if not missing_months:
            paid.append(name)
        else:
            owing.append((name, missing_months))

    print("\n--- Dues Status for " + str(current_year) + " (Jan - current month) ---")

    print("\nFully paid up:")
    if paid:
        for name in paid:
            print(name)
    else:
        print("Nobody yet.")

    print("\nStill owing:")
    if owing:
        for name, missing_months in owing:
            print(name + " - missing: " + ", ".join(missing_months))
    else:
        print("Nobody - everyone is fully paid up!")


def show_member_history(records):
    name = input("Member's name: ").strip()

    if name not in records:
        print(name + " is not a registered member.")
        return

    member = records[name]
    print("\n--- " + name + " ---")
    print("Joined: " + member["joined"])

    if not member["payments"]:
        print("No payments recorded yet.")
        return

    print("Payment history:")
    for payment in member["payments"]:
        print(payment["month"] + " - " + str(payment["amount"]) + " (paid on " + payment["date_paid"] + ")")