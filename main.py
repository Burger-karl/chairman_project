from money_book import members, payments, storage


def main():
    records = storage.load_records()

    running = True
    while running:
        print("\n===== Chairman Ade's Money Book =====")
        print("1. Add new member")
        print("2. List members")
        print("3. Record a payment")
        print("4. Check who has paid / who is owing")
        print("5. View one member's history")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            members.add_member(records)
            storage.save_records(records)

        elif choice == '2':
            members.list_members(records)

        elif choice == '3':
            payments.record_payment(records)
            storage.save_records(records)

        elif choice == '4':
            payments.show_owe_status(records)

        elif choice == '5':
            payments.show_member_history(records)

        elif choice == '6':
            running = False
            print("Goodbye, Chairman!")

        else:
            print("Please choose 1-6.")


if __name__ == '__main__':
    main()