# Chairman Ade's Money Book

A simple program for Chairman Ade to keep track of estate dues for members who has
joined, who has paid, and who is still owing. Records are saved to disk, so
nothing is lost when the program is closed.

## How to Start

1. Open a terminal in this project folder.
2. Run:

   ```
   python main.py
   ```

3. Choose an option from the menu (1-6) and follow the prompts.

No setup is needed the first time you run it, if there are no saved
records yet, the program just starts fresh.

## Project Layout

```
chairman_project/
|-- main.py                 <- run this file to start the program
|-- README.md                <- this file
|-- data/                    <- created automatically, holds saved records
|   |-- records.json
|   |-- diary.log
|-- money_book/               <- the package containing all the program's logic
    |-- __init__.py
    |-- storage.py
    |-- diary.py
    |-- members.py
    |-- payments.py
```

## What Each File Does

- **main.py**: The menu. This is the only file you run. It shows the
  options, asks what you want to do, and calls the right function in
  `money_book/`. It doesn't do any of the actual work itself.

- **money_book/storage.py**: Loads `data/records.json` into memory when
  the program starts, and saves it back to disk whenever something
  changes. If the file doesn't exist yet, it starts with an empty
  record. If the file is damaged or unreadable, it starts fresh instead
  of crashing.

- **money_book/diary.py**: Keeps `data/diary.log`, a plain text file
  that notes down what happened and when (new members, payments). Every
  entry is added to the bottom of the file, nothing already written is
  ever erased.

- **money_book/members.py**: Adds new members and lists everyone who has
  joined.

- **money_book/payments.py**: Records a payment for a member, shows who
  has paid and who is still owing for the current month, and shows one
  member's full payment history.

- **data/records.json**: The saved data itself: every member, when
  they joined, and every payment they've made. You don't need to open
  this file yourself; the program reads and writes it automatically.

- **data/diary.log**: A plain text diary you can open and read on your
  own, even without running the program.

## Menu Options

1. **Add new member**: register someone new.
2. **List members**: see everyone who has joined.
3. **Record a payment**: log a payment for a member, with the month and
   amount.
4. **Check who has paid / who is owing**: see the current month's
   status for everyone.
5. **View one member's history**: see everything one person has ever
   paid.
6. **Exit**: close the program. Everything you've entered is already
   saved.