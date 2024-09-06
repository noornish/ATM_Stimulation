class ATM:
    balance = 0
    pin = "1234"
    transaction_history = []

    @classmethod
    def check_pin(cls, input_pin):
        return input_pin == cls.pin

    @classmethod
    def change_pin(cls, old_pin, new_pin):
        if cls.check_pin(old_pin):
            cls.pin = new_pin
            cls.transaction_history.append("PIN changed")
            print("PIN successfully changed.")
        else:
            print("Incorrect old PIN.")

    @classmethod
    def deposit(cls, amount):
        if amount > 0:
            cls.balance += amount
            cls.transaction_history.append(f"Deposited: ${amount}")
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount.")

    @classmethod
    def withdraw(cls, amount):
        if 0 < amount <= cls.balance:
            cls.balance -= amount
            cls.transaction_history.append(f"Withdrew: ${amount}")
            print(f"Withdrew: ${amount}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    @classmethod
    def check_balance(cls):
        cls.transaction_history.append("Checked balance")
        print(f"Current balance: ${cls.balance}")

    @classmethod
    def print_transaction_history(cls):
        print("Transaction History:")
        for transaction in cls.transaction_history:
            print(transaction)

def main():
    ATM.balance = 1000  # Set initial balance to $1000
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            input_pin = input("Enter PIN: ")
            if ATM.check_pin(input_pin):
                ATM.check_balance()
            else:
                print("Incorrect PIN.")
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            ATM.deposit(amount)
        elif choice == "3":
            input_pin = input("Enter PIN: ")
            if ATM.check_pin(input_pin):
                amount = float(input("Enter withdrawal amount: "))
                ATM.withdraw(amount)
            else:
                print("Incorrect PIN.")
        elif choice == "4":
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new PIN: ")
            ATM.change_pin(old_pin, new_pin)
        elif choice == "5":
            ATM.print_transaction_history()
        elif choice == "6":
            print("Exiting ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
