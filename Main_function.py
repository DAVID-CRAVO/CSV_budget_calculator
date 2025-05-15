from Expenses_tracker_avg import load_data, show_summary

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
