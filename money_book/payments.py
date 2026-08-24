from datetime import datetime
from money_book.diary import log_event

def record_payment(records):
    name = input("Member's name: ").strip()

    if name not in records:
        print(name + " is not a registered member.")
        return

    month = input("Which month is this payment for?").strip()
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
        print("No members yet")
        return

    current_month = datetime.now().strftime("%B %Y")

    paid = []
    owing = []

    for name in records:
        has_paid = False
        for payment in records[name]["payments"]:
            if payment["month"] == current_month:
                has_paid = True

        if has_paid:
            paid.append(name)
        else:
            owing.append(name)

    print("\n==== Dues Status for " + current_month + " ====")

    print("\nPaid up:")  
    if paid:
        for name in paid:
            print(name)
    else:
        print("Nobody yet.")

    print("\nStill owing:")
    if owing:
        for name in owing:
            print(name)
    else: 
        print("Nobody - everyone has paid!")


def show_member_history(records):
    name = input("Member's name: ").strip()

    if name not in records:
        print(name + " is not a registered member.")
        return

    member = records[name]
    print("\n==== " + name + "====")
    print("Joined: " + member["joined"])

    if not member["payments"]:
        print("No payments recorded yet")
        return

    print("Payment history:")
    for payment in member["payments"]:
        print(payment["month"] + " - " + str(payment["amount"]) + " (paid on " + payment["date_paid"] + ")")
