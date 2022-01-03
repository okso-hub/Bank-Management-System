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
    print(f"Success! Your balance is {int_balance}.")



def deposit():
    pass


def main():
    clear()
    # create_account(
    #     str(input("Enter your full name: ")),
    #     str(input("Enter your birthday (ddmmyy): ")),
    #     int(input("Enter your balance: ")),
    #     str(input("Enter the country you live in: "))
    # )

    log_in(
        str(input("Enter your name: ")),
        int(input("Enter four digit code: "))
    )
    withdraw(int(input("Enter withdraw amount: ")))


if __name__ == "__main__":
    main()
