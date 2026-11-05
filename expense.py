

from datetime import datetime


def add_expense():
  print("\nadd new expense")

  while True:
    expense_date = input("enter date (YYYY-MM-DD): ")
    try:
      datetime.strptime(expense_date, "%Y-%m-%d")
      break
    except ValueError:
      print("wrong date. please try this again.")

  category = input("Enter category: ")
  while category == "":
    print("category cannot be empty.")
    category = input("enter category: ")

  description = input("enter description: ")
  while True:
    try:
      amount = float(input("enter amount: "))
      if amount > 0:
        break
      print("amount must be greater than zero.")
    except ValueError:
      print("please enter a number.")

  expense = {
    "date": expense_date,
    "category": category,
    "description": description,
    "amount": amount
  }

  print("expense added successfully.")
  return expense


def print_expenses(expenses):
  if not expenses:
    print("there are no expenses to display.")
    return

  total = 0
  for expense in expenses:
    print("\n--------------------")
    print("date:", expense["date"])
    print("category:", expense["category"])
    print("description:", expense["description"])
    print("amount: $", format(expense["amount"], ".2f"))
    total += expense["amount"]

  print("\n--------------------")
  print("total amount: $", format(total, ".2f"))
  print("total expenses:", len(expenses))