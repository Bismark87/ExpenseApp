

from expense import add_expense, print_expenses
from file import export_expenses, load_expenses, save_expenses
from expensefiltter import filter_expenses

expenses = []

while True:
    print("\n==== expense manager ====")
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
    elif choice == "2":
        print_expenses(expenses)
    elif choice == "3":
        filename = input("Enter file name: ")
        if filename == "":
            filename = "expenses.json"
        if not filename.endswith(".json"):
            filename += ".json"
        save_expenses(expenses, filename)
    elif choice == "4":
        filename = input("Enter file name: ")
        if filename == "":
            filename = "expenses.json"
        if not filename.endswith(".json"):
            filename += ".json"
        new_expenses = load_expenses(filename)
        if new_expenses is not None:
            expenses = new_expenses
    elif choice == "5":
        print("\nfilter expenses")
        start_date = input("enter starting date or press Enter to skip: ")
        end_date = input("enter ending date or press Enter to skip: ")
        category = input("enter category or press Enter to skip: ")
        results = filter_expenses(
            expenses,
            start_date,
            end_date,
            category
        )
        if results is not None:
            print("\nsearch results:")
            print_expenses(results)
    elif choice == "6":
        filename = input("Enter CSV file name: ")
        if filename == "":
            filename = "expenses.csv"
        if not filename.endswith(".csv"):
            filename += ".csv"
        export_expenses(expenses, filename)
    elif choice == "7":
        print("Thanks for using expense manager.")
        break
    else:
        print("Invalid choice. please try again.")
