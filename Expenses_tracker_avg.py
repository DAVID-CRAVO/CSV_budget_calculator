#Fullly functional final product!!!!
import csv
from collections import defaultdict

# Load data from CSV file to the algorithm
def load_data(filename):
    data = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount'])
                data.append(row)
        print(f"Loaded {len(data)} transactions.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")
    return data

# Sorting expenses by category
def summarize_by_category(data):
    summary = defaultdict(float)
    for row in data:
        summary[row['category']] += row['amount']
    return summary

# Save summary to a new CSV file
def save_summary(summary, total, avg, filename='category_summary.csv'):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Category', 'Amount'])
            for category, amount in summary.items():
                writer.writerow([category, f"{amount:.2f}"])
            writer.writerow(['Total', f"{total:.2f}"])
            writer.writerow(['Average spent', f"{avg:.2f}"])
        print(f"Summary saved to '{filename}'.")
    except Exception as e:
        print(f"Failed to save summary: {e}")

# Display and save summary
def show_summary(data):
    if not data:
        print("No data to show.")
        return

    summary = summarize_by_category(data)
    total = sum(summary.values())
    average = total /len(data)

    print("\nSummary by transaction:")
    for category, amount in summary.items():
        print(f"{category}: ${amount:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Average spent: ${average:.2f}")

    save_summary(summary, total, average)

# Main function
def main():
    filename = "budgets.csv"
    data = load_data(filename)

    if not data:
        return

    while True:
        choice = input("\nOptions:\n1. View Summary\n2. Exit\nChoose: ")
        if choice == '1':
            show_summary(data)
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
