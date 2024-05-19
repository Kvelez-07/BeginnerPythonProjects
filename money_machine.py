def atm():
    print("Welcome to the ATM!")
    
    while True:
        try:
            balance = float(input("Enter your balance: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for your balance.")
    
    budget = balance
    expenses = []

    while True:
        print("\n1. Deposit")
        print("\n2. Withdraw")
        print("\n3. View budget")
        print("\n4. View expenses")
        print("\n5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            try:
                amount = float(input("Enter the amount to deposit $: "))
                if amount <= 0:
                    print("Deposit amount must be positive.")
                else:
                    budget += amount
                    print("Deposit successful!")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == 2:
            try:
                amount = float(input("Enter the amount to withdraw $: "))
                if amount <= 0:
                    print("Withdrawal amount must be positive.")
                elif amount > budget:
                    print("Insufficient funds!")
                else:
                    budget -= amount
                    expenses.append(f"Withdrawal: -{amount}")
                    print("Withdrawal successful!")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == 3:
            print("Your budget is $:", budget)
        elif choice == 4:
            if expenses:
                print("Your expenses are $:")
                for expense in expenses:
                    print(expense)
            else:
                print("No expenses recorded.")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

        print("Current budget:", budget)

        if budget < 0:
            print("You have exceeded your budget. You have incurred", -budget, "in debt.")

    print("Goodbye!")

if __name__ == "__main__":
    atm()