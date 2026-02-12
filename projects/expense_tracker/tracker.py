import csv
from datetime import datetime
from pathlib import Path

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        if not Path(self.filename).exists():
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Description", "Amount"])

    def add_expense(self, description, amount):
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, description, amount])
        print(f"💰 Logged: {description} (${amount})")

    def show_summary(self):
        print("\n--- 💸 Your Spending Summary ---")
        total = 0
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(f"{row['Date']} | {row['Description']}: ${row['Amount']}")
                total += float(row['Amount'])
        print(f"Total Spent: ${total:.2f}")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense("Coffee", 4.50)
    tracker.add_expense("Python Book", 25.00)
    tracker.show_summary()
