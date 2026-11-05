

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

def load_expenses(filename):
     try:
         file = open(filename, "r")
         expenses = json.load(file)

        file.close()
       if isinstance(expenses, list):
       print("Expenses opened successfully.")

            return expenses
          else:
       print("The file does not contain an expense list.")
         return None

    except FileNotFoundError:
          print("File not found.")
            return None

    except json.JSONDecodeError:
         print("The file contains incorrect JSON information.")

        return None

    except OSError:
        print("Unable to open the file.")
        return None

def export_expenses(expenses, filename):
       try:
        file = open(filename, "w", newline="")
         writer = csv.writer(file)

        writer.writerow(["Date", "Category", "Description", "Amount"])

        for expense in expenses:

            writer.writerow([
                expense["date"],
                expense["category"],
                expense["description"],
                expense["amount"]
            ])
          file.close()
        print("CSV file created successfully.")

    except OSError:
print("Unable to create CSV file.")
