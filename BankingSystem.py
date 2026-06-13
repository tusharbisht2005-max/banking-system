def show_balance(Balance):
    print(f"Your current balance is: ${Balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit: "))
    if amount < 0:
        print(f"That's not a valid amount. Please enter a positive number.")
        return 0
    else:
        return amount

def withdraw(Balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > Balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print(f"Amount must be greater than zero")
        return 0
    else:
        return amount

def main():
    Balance = 0.0
    while True:
        print("\nWelcome to the Banking System")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Please select an option (1-4): ")

        if choice == '1':
            show_balance(Balance)
           
        elif choice == '2':
            Balance += deposit()
            show_balance(Balance)
        elif choice == '3':
            Balance -= withdraw(Balance)
            show_balance(Balance)

        elif choice == '4':
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()