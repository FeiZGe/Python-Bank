def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("===========================")
        print("Insufficient funds")
        print("===========================")
        return 0
    elif amount < 0:
        print("===========================")
        print("Amount must be greater than 0")
        print("===========================")
        return 0
    else:
        return amount
