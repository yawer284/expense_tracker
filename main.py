import argparse
from models import (
    add_expense,
    delete_expense,
    updated_expense,
    list_expense,
    get_summary
)

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI Application")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True, type=str, help="Description of the expense")
    add_parser.add_argument("--amount", required=True, type=float, help="Amount of the expense")
    add_parser.add_argument("--category", type=str, default="General", help="Category (default: General)")

    #update command
    update_parser = subparsers.add_parser("update", help="Update a existing expense")
    update_parser.add_argument("--id", required=True, type=int, help="ID of the expense")
    update_parser.add_argument("--description", type=str, help="New description")
    update_parser.add_argument("--amount", type=float, help="New amount")

    # delete command
    delete_parser =  subparsers.add_parser("delete", help="Delete an expense by ID")
    delete_parser.add_argument("--id", required=True, type=int, help="ID of the expense")

    # list command
    list_parser = subparsers.add_parser("list", help="List all expense")
    list_parser.add_argument("--category", type=str, help="Filter expense by category")

    # summary command
    summary_parser = subparsers.add_parser("summary", help="Show total expense summary")
    summary_parser.add_argument("--month", type=int, help="Filter summary by month (1-12)")

    # take the input from the user and save it as an object
    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount, args.category)
    elif args.command == "update":
        updated_expense(args.id, args.description, args.amount)
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "list":
        list_expense(args.category)
    elif args.command == "summary":
        get_summary(args.month)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()