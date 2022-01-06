from random import randint
import os


def clear(): return os.system("clear") if os.name == "posix" else os.system("cls")


def create_account(name, birthday, balance, address):
    # Generating the login code
    global code
    code = ""
    for i in range(4):
        code += str(randint(0, 9))
    int(code)

    # Generating the IBAN
    iban = ""
    for i in range(22):
        iban += str(randint(0, 9))
    IBAN = f"DE {int(iban)}"

    # Saving information on a textfile
    with open(f"{name}.txt", "w") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Date of birth: {birthday}\n")
        f.write(f"Address: {address}\n")
        f.write(f"Code: {code}\n")
        f.write(f"Balance: {balance}\n")
        f.write(f"IBAN: {IBAN}\n")


def log_in(name, input_code):
    # Setting a global account name for login
    global account_name
    account_name = name

    # Reading and outputting the information
    try:
        with open(f"{name}.txt", "r") as f:
            lines = f.readlines()

            balance_line = lines[4]
            split_balance_line = balance_line.split(" ")
            balance = split_balance_line[1].replace("\n", "")

            code_line = lines[3]
            split_code_line = code_line.split(" ")
            code = int(split_code_line[1])

        if input_code == code:
            clear()
            print(f"Success. Welcome, {name} your balance is {balance}.")
        else:
            print("Failure. Wrong code.")
    except:
        print("Account does not exist.")


def withdraw(withdraw_amount):
    # Reading the balance from textfile
    with open(f"{account_name}.txt", "r") as f:
        lines = f.readlines()

        balance_line = lines[4]
        split_balance_line = balance_line.split(" ")
        balance = split_balance_line[1].replace("\n", "")

        int_balance = int(balance)

        int_balance -= withdraw_amount

    # Updating balance on textfile
    lines[4] = f"Balance: {int_balance}\n"

    with open(f"{account_name}.txt", "w") as f:
        f.writelines(lines)

    # Outputting balance
    clear()
    print(f"Success! Your balance is ${int_balance}.")


def deposit(deposit_amount):
    # Reading the balance from textfile
    with open(f"{account_name}.txt", "r") as f:
        lines = f.readlines()

        balance_line = lines[4]
        split_balance_line = balance_line.split(" ")
        balance = split_balance_line[1].replace("\n", "")

        int_balance = int(balance)

        int_balance += deposit_amount

    # Updating balance on textfile
    lines[4] = f"Balance: {int_balance}\n"

    with open(f"{account_name}.txt", "w") as f:
        f.writelines(lines)

    # Outputting balance
    clear()
    print(f"Success! Your balance is ${int_balance}.")


def change_code(old_code):
    # Reading the code from the textfile
    with open(f"{account_name}.txt", "r") as f:
        lines = f.readlines()

        code_line = lines[3]
        split_code_line = code_line.split(" ")
        code = split_code_line[1].replace("\n", "")

    # Checking if the the user knows the current code
    if old_code == int(code):
        new_code = int(input("Enter your new code: "))
        lines[3] = f"Code: {new_code}\n"

        with open(f"{account_name}.txt", "w") as f:
            f.writelines(lines)

        clear()
        print(f"Success! You successfully changed your code from {code} to {new_code}.")
    else:
        clear()
        print(f"{old_code} is not your current code. Please try again.")


def view_information():
    pass


def transfer(destination_account):
    pass


def main():
    while True:
        clear()
        print("--- ATM Please select an option to continue ---")
        print("1. Create a new account \n2. Log in to an existing account")
        mode = int(input(""))

        if mode == 1:
            clear()
            create_account(
                str(input("Enter your full name: ")),
                str(input("Enter your birthday: ")),
                int(input("Enter your balance: $")),
                str(input("Enter the region you live in: "))
            )

            logged_in = True

            while logged_in:
                print("--- ATM Please select an option to continue ---")
                print("1. Withdraw money from your bank account \n2. Deposit money to your bank account \n3. Log out")
                option = int(input(""))

                if option == 1:
                    withdraw(int(input("Enter your withdraw amount: ")))
                elif option == 2:
                    deposit(int(input("Enter your deposit amount: ")))
                elif option == 3:
                    logged_in = False

        elif mode == 2:
            clear()
            log_in(
                str(input("Enter your full name: ")),
                int(input("Enter your code: "))
            )

            logged_in = True

            while logged_in:
                print("--- ATM Please select an option to continue ---")
                print("1. Withdraw money from your bank account \n2. Deposit money to your bank account \n3. Change code \n4. Log out")
                option = int(input(""))

                if option == 1:
                    withdraw(int(input("Enter your withdraw amount: ")))
                elif option == 2:
                    deposit(int(input("Enter your deposit amount: ")))
                elif option == 3:
                    change_code(int(input("Enter your current code: ")))
                elif option == 4:
                    break

        elif mode == 3:
            break


if __name__ == "__main__":
    main()
