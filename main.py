from random import randint

def create_account(name, birthday, balance, address):

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
        print(new_birthday)
    

    # Saving information on a textfile
    with open(f"{name}.txt", "w") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Date of birth: {new_birthday}\n")
        f.write(f"Address: {address}\n")
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
    create_account("test", "150108", 5000, "Germany")
    # main()

