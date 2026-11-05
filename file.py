

import csv
import json


def save_expenses(expenses, filename):
  try:
    with open(filename, "w", encoding="utf-8") as file:
      json.dump(expenses, file, indent=4)
    print("Expenses saved successfully.")
  except OSError:
    print("Unable to save the file.")

def load_expenses(filename):
  try:
    with open(filename, "r", encoding="utf-8") as file:
      expenses = json.load(file)
  except FileNotFoundError:
    print("File not found.")
    return None
  except json.JSONDecodeError:
    print("The file contains incorrect JSON information.")
    return None
  except OSError:
    print("Unable to open the file.")
    return None

  if not isinstance(expenses, list):
    print("The file does not contain an expense list.")
    return None

  print("Expenses opened successfully.")
  return expenses


def export_expenses(expenses, filename):
  try:
    with open(filename, "w", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(["Date", "Category", "Description", "Amount"])
      for expense in expenses:
        writer.writerow([
          expense["date"],
          expense["category"],
          expense["description"],
          expense["amount"]
        ])
    print("CSV file created successfully.")
  except OSError:
    print("Unable to create CSV file.")
