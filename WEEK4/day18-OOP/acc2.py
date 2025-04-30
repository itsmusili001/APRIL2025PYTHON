import Account

def get_menu_choice():
    print()
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Get Account balance")

    choice=int(input("Enter your choice: "))
    return choice

def main():
    accName = input("Enter account name: ")
    accNo = input("Enter account number: ")
    accBal = float(input("Enter account balance: "))
    

    account = Account.Account(accNo, accName, accBal)

    choice=0
    while choice != 3:
        choice = get_menu_choice()
        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 3:
            print("Account balance: ", account.getAccBal())
        else:
            print("Invalid choice")

main()