
from datetime 
import datetime


def filter_expenses(expenses, start_date, end_date, category):

    if start_date != "":
         try:
    datetime.strptime(start_date, "%Y-%m-%d")
          except ValueError:
            print("invalid starting date.")
            return None

    if end_date != "":
         try:
            datetime.strptime(end_date, "%Y-%m-%d")

        except ValueError:
            print("invalid ending date.")
            return None

    if start_date != "" and end_date != "":

        if start_date > end_date:
            print("starting date cannot be after ending date.")
            return None

    results = []

    for expense in expenses:

        date_is_correct = True
        category_is_correct = True

        if start_date != "":
              if expense["date"] < start_date:
                date_is_correct = False

        if end_date != "":
               if expense["date"] > end_date:
                date_is_correct = False

        if category != "":

            if expense["category"].lower() != category.lower():
                category_is_correct = False

        if date_is_correct and category_is_correct:

            results.append(expense)

    return results