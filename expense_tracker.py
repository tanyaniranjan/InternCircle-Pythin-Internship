import csv
import os

FILE_NAME = "expenses.csv"


def create_csv_file():
    """Creates the CSV file and adds headings when it is not present."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


def add_expense():
    """Takes expense input from the user and stores it in the CSV file."""
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully.")


def view_expenses():
    """Displays every saved expense."""
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        print("\n--- All Expenses ---")
        for row in reader:
            print(" | ".join(row))


def filter_expenses():
    """Shows expenses belonging to a selected category."""
    selected_category = input("Enter category to filter: ").strip().lower()
    found = False

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        print(f"\n--- Expenses in {selected_category.title()} ---")

        for row in reader:
            if row["Category"].strip().lower() == selected_category:
                print(
                    f"Date: {row['Date']} | "
                    f"Amount: Rs. {row['Amount']} | "
                    f"Description: {row['Description']}"
                )
                found = True

    if not found:
        print("No expenses found in this category.")


def show_category_summary():
    """Calculates and displays the total expense for each category."""
    category_totals = {}

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"].strip()
            amount = float(row["Amount"])

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    print("\n--- Category-wise Expense Summary ---")

    if not category_totals:
        print("No expenses recorded yet.")
    else:
        for category, total in category_totals.items():
            print(f"{category}: Rs. {total:.2f}")


def main():
    create_csv_file()

    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Filter expenses by category")
        print("4. Show category-wise summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            show_category_summary()
        elif choice == "5":
            print("Thank you for using Personal Expense Tracker.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
