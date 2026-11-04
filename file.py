

import json
import csv

def save_expenses(expenses, filename):

    try:
    file = open(filename, "w")
    json.dump(expenses, file, indent=4)
    file.close()
print("Expenses saved successfully.")

except OSError:
 print("unable to save the file.")
