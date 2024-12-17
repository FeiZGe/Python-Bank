def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("===========================")
        print("That's not a valid amount")
        print("===========================")
        return 0
    else:
        return amount
