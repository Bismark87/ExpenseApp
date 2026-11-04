

from expense 
import add_expense
from expense 
import print_expenses

from file_manager 
import save_expenses
from file_manager 
import load_expenses
from file_manager 
import export_expenses

from filter_expenses 
import filter_expenses

expenses = []

while True:

    print("\n==== Expense Manager ====")

    print("1. add expense")
    print("2. view expenses")
    print("3. save expenses")
    print("4. open expense file")
    print("5. filter expenses")
    print("6. export expenses to csv")
    print("7. exit")

    print("====")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_expense = add_expense()
        expenses.append(new_expense)
