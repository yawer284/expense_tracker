# Expense Tracker CLI

A command-line application to manage your personal finances.
Track expenses by category, set monthly budgets, and export
your data to CSV.

---

## Features
- Add, update, and delete expenses
- Categorize expenses and filter by category
- View total or monthly expense summaries
- Set a monthly budget with overspending warnings
- Export expenses to CSV

---

## Installation

```bash
git clone https://github.com/abdallah-m-fawzy/expense-tracker
cd expense-tracker
pip install -e .
```

---

## Usage

```bash
expense-tracker add --description "Lunch" --amount 20 --category "Food"
# Expense added successfully (ID: 1)

expense-tracker list
# ID   Date         Description   Amount   Category
# 1    2024-08-06   Lunch         $20.0    Food

expense-tracker summary
# Total expenses: $20.0

expense-tracker summary --month 8
# Total expenses for August: $20.0

expense-tracker delete --id 1
# Expense deleted successfully
```

---

## Project Structure

```
expense-tracker/
├── main.py       # CLI commands (argparse)
├── models.py     # Core logic (add, delete, update, summary)
├── storage.py    # JSON file I/O and validation
└── setup.py      # Package setup for the expense-tracker command
```

---

## Tech Stack
- Python 3
- argparse
- JSON for data storage