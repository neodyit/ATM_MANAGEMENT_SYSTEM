balance = 5000
statement = []

while True:
    print("\n===== ATM MENU =====")
    print("1. Display Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"\nYour current balance is: ₹{balance}")

    elif choice == "2":
        amount = int(input("Enter amount to withdraw: ₹"))

        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            statement.append(f"Withdrawn: ₹{amount}")
            print(f"₹{amount} withdrawn successfully.")
            print(f"Remaining balance: ₹{balance}")

    elif choice == "3":
        amount = int(input("Enter amount to deposit: ₹"))

        if amount <= 0:
            print("Invalid amount.")
        else:
            balance += amount
            statement.append(f"Deposited: ₹{amount}")
            print(f"₹{amount} deposited successfully.")
            print(f"Updated balance: ₹{balance}")

    elif choice == "4":
        print("\n===== Transaction Statement =====")
        if len(statement) == 0:
            print("No transactions yet.")
        else:
            for i, record in enumerate(statement, start=1):
                print(f"{i}. {record}")
            print(f"Current Balance: ₹{balance}")

    elif choice == "5":
        print("Thank you for using ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")