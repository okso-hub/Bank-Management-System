from random import randint
import os
from time import sleep
from simple_term_menu import TerminalMenu


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
    if address.lower() == "germany":
        IBAN = f"DE {int(iban)}"
    elif address.lower() == "usa" or "us" or "america":
        IBAN = f"US {int(iban)}"
    
    # Choosing the currency
    global currency
    if address.lower() == "germany":
        currency = "€"
    elif address.lower() == "usa" or "us" or "america":
        currency = "$"
    elif address.lower() == "uk" or "britain" or "england":
        currency = "£"

    # Setting a global account name for login
    global account_name
    account_name = name

    # Saving information on a textfile
    with open(f"accounts/{name}.txt", "w") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Date of birth: {birthday}\n")
        f.write(f"Address: {address}\n")
        f.write(f"Code: {code}\n")
        f.write(f"Balance: {currency}{balance}\n")
        f.write(f"IBAN: {IBAN}\n")

    clear()
    print(f"Success. Welcome, {name} your balance is {currency}{balance}.")


def log_in(name, input_code):
    # Setting a global account name for login
    global account_name
    account_name = name

    global currency

    # Reading and outputting the information
    try:
        with open(f"accounts/{name}.txt", "r") as f:
            lines = f.readlines()

            balance_line = lines[4]
            split_balance_line = balance_line.split(" ")
            currency = split_balance_line[1][0]
            balance = split_balance_line[1].replace("\n", "").replace(f"{currency}", "")

            code_line = lines[3]
            split_code_line = code_line.split(" ")
            code = int(split_code_line[1])

        global LOG
        if input_code == code:
            LOG = True
            clear()
            print(f"Success. Welcome, {name} your balance is {currency}{balance}.")
        else:
            LOG = False
            print("Failure. Wrong code.")
    except:
        print("Account does not exist.")


def withdraw(withdraw_amount):
    # Reading the balance from textfile
    with open(f"accounts/{account_name}.txt", "r") as f:
        lines = f.readlines()

        balance_line = lines[4]
        split_balance_line = balance_line.split(" ")
        balance = split_balance_line[1].replace("\n", "").replace(f"{currency}", "")

        int_balance = int(balance)

        int_balance -= withdraw_amount

    # Updating balance on textfile
    lines[4] = f"Balance: {currency}{int_balance}\n"

    with open(f"accounts/{account_name}.txt", "w") as f:
        f.writelines(lines)

    # Outputting balance
    clear()
    print(f"Success! Your balance is {currency}{int_balance}.")


def deposit(deposit_amount):
    # Reading the balance from textfile
    with open(f"accounts/{account_name}.txt", "r") as f:
        lines = f.readlines()

        balance_line = lines[4]
        split_balance_line = balance_line.split(" ")
        balance = split_balance_line[1].replace("\n", "").replace(f"{currency}", "")

        int_balance = int(balance)

        int_balance += deposit_amount

    # Updating balance on textfile
    lines[4] = f"Balance: {currency}{int_balance}\n"

    with open(f"accounts/{account_name}.txt", "w") as f:
        f.writelines(lines)

    # Outputting balance
    clear()
    print(f"Success! Your balance is {currency}{int_balance}.")


def change_code(old_code):
    # Reading the code from the textfile
    with open(f"accounts/{account_name}.txt", "r") as f:
        lines = f.readlines()

        code_line = lines[3]
        split_code_line = code_line.split(" ")
        code = split_code_line[1].replace("\n", "")

    # Checking if the the user knows the current code
    if old_code == int(code):
        new_code = int(input("Enter your new code: "))
        lines[3] = f"Code: {new_code}\n"

        with open(f"accounts/{account_name}.txt", "w") as f:
            f.writelines(lines)

        clear()
        print(f"Success! You successfully changed your code from {code} to {new_code}.")
    else:
        clear()
        print(f"{old_code} is not your current code. Please try again.")


def view_information():
    with open(f"accounts/{account_name}.txt", "r") as f:
        content = f.read()

    clear()
    print(content)


def transfer(transfer_name, transfer_iban, transfer_amount):
    with open(f"accounts/{account_name}.txt", "r") as f:
        lines = f.readlines()
        balance_line = lines[4]
        split_balance_line = balance_line.split(" ")
        balance = int(split_balance_line[1].replace("\n", "").replace(f"{currency}", ""))

    try:
        with open(f"accounts/{transfer_name}.txt", "r") as f:
            transfer_lines = f.readlines()
            iban_line = transfer_lines[5]
            split_iban_line = iban_line.split(" ")
            iban = int(split_iban_line[2])

            transfer_balance_line = transfer_lines[4]
            split_balance_line = transfer_balance_line.split(" ")
            transfer_balance = int(split_balance_line[1].replace("\n", "").replace(f"{currency}", ""))

        if transfer_iban == iban:
            balance -= transfer_amount
            lines[4] = f"Balance: {currency}{balance}\n"

            transfer_balance += transfer_amount
            transfer_lines[4] = f"Balance: {currency}{transfer_balance}\n"

            with open(f"accounts/{account_name}.txt", "w") as f:
                f.writelines(lines)

            with open(f"accounts/{transfer_name}.txt", "w") as f:
                f.writelines(transfer_lines)

            clear()
            print(f"You have successfully transferred {currency}{transfer_amount} to {transfer_name}.")

        else:
            clear()
            print("Wrong IBAN.")
            return

    except:
        clear()
        print("Destination account couldn't be found.")


def main():
    options = ["Create new account", "Log into an existing account", "Quit ATM"]
    terminal_menu = TerminalMenu(options)
    while True:
        clear()
        print("--- ATM Please select an option to continue ---")
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == 0:
            clear()
            create_account(
                str(input("Enter your full name: ")),
                str(input("Enter your birthday: ")),
                int(input("Enter your balance: ")),
                str(input("Enter the region you live in: "))
            )

            logged_in = True
            logged_options = ["Withdraw money from your bank account", "Deposit money to your bank account", "Change code", "View account information", "Transfer money", "Log out"]
            logged_index = TerminalMenu(logged_options)
            while logged_in:
                print("--- ATM Please select an option to continue ---")
                logged_index_entry = logged_index.show()

                if logged_index_entry == 0:
                    withdraw(int(input("Enter your withdraw amount: ")))
                elif logged_index_entry == 1:
                    deposit(int(input("Enter your deposit amount: ")))
                elif logged_index_entry == 2:
                    change_code(int(input("Enter your current code: ")))
                elif logged_index_entry == 3:
                    view_information()
                elif logged_index_entry == 4:
                    transfer(
                        str(input("Enter name of destination account: ")),
                        int(input("Enter IBAN of destination account: ")),
                        int(input("Enter transfer amount: "))
                    )
                elif logged_index_entry == 5:
                    logged_in = False

        elif menu_entry_index == 1:
            clear()
            log_in(
                str(input("Enter your full name: ")),
                int(input("Enter your code: "))
            )
            logged_in = True if LOG else False
            if not logged_in:
                clear()
                print("Wrong code. You will be redirected to the main menu.")
                sleep(3.5)

            logged_options = ["Withdraw money from your bank account", "Deposit money to your bank account", "Change code", "View account information", "Transfer money", "Log out"]
            logged_index = TerminalMenu(logged_options)
            while logged_in:
                print("--- ATM Please select an option to continue ---")
                logged_entry_index = logged_index.show()

                if logged_entry_index == 0:
                    withdraw(int(input("Enter your withdraw amount: ")))
                elif logged_entry_index == 1:
                    deposit(int(input("Enter your deposit amount: ")))
                elif logged_entry_index == 2:
                    change_code(int(input("Enter your current code: ")))
                elif logged_entry_index == 3:
                    view_information()
                elif logged_entry_index == 4:
                    transfer(
                        str(input("Enter name of destination account: ")),
                        int(input("Enter IBAN of destination account: ")),
                        int(input("Enter transfer amount: "))
                    )
                elif logged_entry_index == 5:
                    logged_in = False

        elif menu_entry_index == 2:
            break


if __name__ == "__main__":
    main()
