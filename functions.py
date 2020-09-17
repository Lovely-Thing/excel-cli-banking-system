import pyinputplus as pyip
import bank_operations_ui 
import sys


operations = {
    "Open New Account":bank_operations_ui.BankOperationsUi.open_account,
    "Withdraw Money": bank_operations_ui.BankOperationsUi.withdraw_money,
    "Deposit Money":bank_operations_ui.BankOperationsUi.deposit_money,
    "Check Clients & Balance":bank_operations_ui.BankOperationsUi.check_balance,
    "Delete an Account" :bank_operations_ui.BankOperationsUi.delete_account
    }


def check_choice(choice):
    '''This Function is going to call the desired function based of user choice.'''
    if choice in operations:
        operations[choice]()
    elif choice.lower() == "quit":
        sys.exit()


def start_program():
    print("---------------------------------------------")
    choice = pyip.inputMenu(
    ["Open New Account", "Withdraw Money", "Deposit Money", "Check Clients & Balance","Delete an Account","Quit"]
    ,numbered=True)
    check_choice(choice)