from datetime import datetime
from storage import load_data, save_data

def add_expense(description, amount, category = "General"):
    #make sure the amount of expense that we entered must be bigger than 0
    if amount <= 0:
        print("Error: Amount must be greater than 0.")
        return False

    data = load_data()
    expenses = data["expenses"]

    #this if-else statement checks if the id == 0 or not if not add a new id with one higher num
    if len(expenses) == 0:
        new_id = 1
    else:
        new_id = expenses[-1]["id"] + 1

    #get the current date when you enter the the expense
    today_date = datetime.now().strftime("%Y-%m-%d")

    new_expense = {
        "id": new_id,
        "date": today_date,
        "description": description,
        "amount": float(amount),
        "category": category
    }

    #add the new dict date to the expenses in the json file by the load_data function
    expenses.append(new_expense)

    #save the data that we entered by using the save_data function
    if save_data(data):
        print("Expense added successfully (ID: {})".format(new_id))
        return True
    return False

def delete_expense(expense_id):
    data = load_data()
    expenses = data["expenses"]

    #if id == expense_id then don't take it in the new updated_expense list
    updated_expenses = [e for e in expenses if e["id"] != expense_id]

    #if the len of the list still the same then the id is not found
    if len(updated_expenses) == len(expenses):
        print("Error: Expense with ID {} not found".format(expense_id))
        return False

    data["expenses"] == updated_expenses
    if save_data(data):
        print("Expense deleted successfully")
        return True
    return False

#I set the description and amount to None so it's not necessary must to change
def updated_expense(expense_id, description = None, amount = None):
    data = load_data()

    for expense in data["expenses"]:
        if expense["id"] == expense_id: #make sure that the expense_id that the user entered == to the expense["id"] that in the json file
            if description is not None: #if description is not empty
                expense["description"] = description #then replace it with the new description
            if amount is not None: #if amount is not empty
                if float(amount) <= 0: #if amount is less than 0.
                    print("Error: Amount must eb greater than 0.")
                    return False
                expense["amount"] = float(amount) #if amount is bigger than 0. then replace it in the json file with the new amount

            save_data(data)
            print("Expense (ID: {}) updated successfully".format(expense_id))
            return True

    print("Expense with (ID: {}) is not found!".format(expense_id))
    return False

def list_expense(category = None):
    data = load_data()
    expenses = data["expenses"]

    if category:
        expenses = [e for e in expenses if e.get("category", "").lower() == category.lower()] #the .get function get the key values from the dict and if there is no value return it empty

    if not expenses:
        print("No expenses found.")
        return

    #table header
    print("{:<5}{:<20}{:<20}{:<10}{:<20}".format('ID', 'Date', 'Description', 'Amount', 'category'))
    print('-' * 60)

    #table data
    for e in expenses:
        print("{:<5}{:<12}{:<20}{:<9.2f}{:<10}".format(e["id"], e["date"], e["description"], e["amount"], e.get("category", "General")))

def get_summary(month = None, year = None):
    data = load_data()
    expenses = data["expenses"]

    target_year = year if year is not None else datetime.now().year #if you didn't choose year then print current year 

    if month is not None:
        if not (1 <= month <= 12):
            print("Error: Month must be between 1 and 12.")
            return

        total = 0.0

        for e in expenses:
            e_date = datetime.strptime(e["date"], "%Y-%m-%d")
            if e_date.month == month and e_date.year == target_year:
                total += e["amount"]

        month_name = datetime(int(target_year, month, 1)).strftime("%B")
        print("Total expenses for {} {}: {:.2f}".format(month_name, target_year, total))

    else:
        total = sum(e["amount"] for e in expenses)
        print("Total expenses: {:.2f}".format(total))