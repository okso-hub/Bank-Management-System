from random import randint
import os
from types import CodeType


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

    # Creating a birthday string
    x = 0
    new_birthday = ""
    for i in range(len(birthday)):
        if (x % 2) != 0:
            if x < 4:
                new_birthday += birthday[i] + "."
            else:
                new_birthday += birthday[i]
        else:
            new_birthday += birthday[i]
        x += 1

    # Saving information on a textfile
    with open(f"{name}.txt", "w") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Date of birth: {new_birthday}\n")
        f.write(f"Address: {address}\n")
        f.write(f"Code: {code}\n")
        f.write(f"Balance: {balance}\n")
        f.write(f"IBAN: {IBAN}\n")


def log_in():
    pass


def withdraw():
    pass


def deposit():
    pass


def main():
    pass


if __name__ == "__main__":
    clear()
    create_account(
        str(input("Enter your full name: ")),
        str(input("Enter your birthday (ddmmyy): ")),
        int(input("Enter your balance: ")),
        str(input("Enter the country you live in: "))
    )
    # main()
