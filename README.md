# Banking System in Python

A simple command-line banking system built using Python. This project allows users to check their balance, deposit money, and withdraw money through a menu-driven interface.

## Features

- Show current balance
- Deposit money
- Withdraw money
- Prevent invalid deposits
- Prevent withdrawals with insufficient funds
- Easy-to-use menu-based system

## How It Works

The program starts with a balance of `0.0` and continuously shows a menu until the user exits.  
Users can:

1. View their current balance
2. Deposit an amount
3. Withdraw an amount
4. Exit the application

## Technologies Used

- Python 3
- Command-line interface

## Code Structure

- `show_balance(balance)`  
  Displays the current account balance.

- `deposit()`  
  Takes deposit input from the user and returns the amount.

- `withdraw(balance)`  
  Takes withdrawal input from the user and checks if enough balance is available.

- `main()`  
  Runs the banking system menu and manages user interaction.

## How to Run

1. Make sure you have Python installed.
2. Save the code in a file named `banking_system.py`.
3. Open terminal or command prompt.
4. Run the program using:

```bash
python banking_system.py
```

## Example Usage

```text
Welcome to the Banking System
1. Show Balance
2. Deposit
3. Withdraw
4. Exit
Please select an option (1-4):
```

## Future Improvements

- Add account holder name
- Save balance to a file or database
- Add transaction history
- Support multiple user accounts
- Add PIN/login security

## Learning Purpose

This project is great for beginners who want to practice:

- Functions
- Loops
- Conditionals
- User input
- Basic error handling

## Author

**[Your Name]**

## License

This project is open source and free to use for learning purposes.
