# Banking Programs
import show as s
import deposit as d
import withdraw as w

def main():
    balance = 0
    is_running = True

    while is_running:
        print("***********************")
        print("    Banking program    ")
        print("***********************")
        print("[1] Show Balance")
        print("[2] Deposit")
        print("[3] Withdraw")
        print("[4] Exit")
        print("***********************")

        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            s.show_balance(balance)
        elif choice == '2':
            balance += d.deposit()
        elif choice == '3':
            balance -= w.withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("===========================")
            print("That is not a valid choice.")
            print("===========================")

    print("===========================")
    print("Thank you! have a nice day!")
    print("===========================")

if __name__ == '__main__':
    main()