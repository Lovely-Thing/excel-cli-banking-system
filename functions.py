import sys
import pyinputplus as pyip
from bank_operations_ui import BankOperationsUi

operations = {
    "Open New Account": BankOperationsUi.open_account,
    "Withdraw Money": BankOperationsUi.withdraw_money,
    "Deposit Money": BankOperationsUi.deposit_money,
    "Check Clients & Balance": BankOperationsUi.check_balance,
    "Delete an Account": BankOperationsUi.delete_account
    }


def check_choice(choice):
    """This function check user choice.

    If the choice is among the choices it calls the desired function for that.
    if the choice is quit then it teminates the program.

    Parameters:
    ----------
    choice: string -- User entered choice

    Return: None
    """
    if choice in operations:
        operations[choice]()
    elif choice.lower() == "quit":
        sys.exit()


def start_program():
    """This Function is used to start the program.
    
    It ask user to choose and option from bank operations. only a few number of
    choices are allowed. If the user choice is among bank operations choices 
    then it call the check_choice() function.

    Return : None
    """
    print("---------------------------------------------")
    choice = pyip.inputMenu(
        [
            "Open New Account", "Withdraw Money", "Deposit Money", 
            "Check Clients & Balance", "Delete an Account", "Quit"
        ]
        , numbered=True)
        
    check_choice(choice)