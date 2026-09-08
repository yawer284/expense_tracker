import os
import json

DATA_FILE = "expense.json"

'''this function read the data from the json file
if the file wasn't exist or there is wrong with the data it return the default value of the data'''
def load_data():
    default_data = {"expenses": [], "budgets": {}}
    if not os.path.exists(DATA_FILE):
        return default_data

    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
        if "expenses" not in data:
            data["expenses"] = []
        if "budgets" not in data:
            data["budgets"] = []
    except (json.JSONDecodeError, PermissionError):
        return default_data

# this function save python dictionary inside the json file
def save_data(data):
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent = 4)
        return True
    except Exception as e:
        print("Error saving data: {}".format(e))
        return False