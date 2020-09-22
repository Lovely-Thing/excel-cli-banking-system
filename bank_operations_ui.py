import re
import pyinputplus as pyip
import messages
from bank_operations_backend import BankOperationsBackend

def raiseNameError(text):
    """This function raise error if name does not match the pattern"""
    pattern = re.compile("[a-zA-Z]")
    if not pattern.match(text):
        raise Exception("Invalid Name Entered")

def raiseAddressError(text):
    """This function raise error if address does not match the pattern"""
    pattern = re.compile("^[a-zA-Z]+[0-9]*")
    if not pattern.match(text):
        raise Exception("Invalid Address Entered")

class BankOperationsUi:
    """This class contains all operations related to bank interface.

    Public Methods:
    --------------
    open_account(): -- collect user inputs for opening account.
    withdraw_mondey(): -- collect user credentials for withdrawing money
    deposit_money(): -- collect user credentials for depositin money
    check_balance(): -- collect user credentials for checking balance
    delete_account(): -- collect user credentials for deletin account
    """

    @staticmethod
    def open_account():
        """This account collect user inputs for opening new account.
        
        Collect User inputs, store that in a list and pass it to the backend
        open account. if the result from the backend is true it restart the 
        program again and if the result if false it call the open_account() 
        method again to collect user information again.

        Return: None
        """
        print("\n")
        print(messages.open_account)
        u_id = pyip.inputInt("Id: ", greaterThan=0)
        name = pyip.inputCustom(raiseNameError, prompt="Name: ")
        address = pyip.inputCustom(raiseAddressError, prompt="Address: ")
        email = pyip.inputEmail("Email: ")
        balance = pyip.inputInt("Balance: ", min=0)
        password = pyip.inputPassword("Password: ")

        user_data = [u_id, name, address, balance, email, password]
        result = BankOperationsBackend.open_account(user_data)

        start_again() if result else BankOperationsUi.open_account()

    @staticmethod
    def withdraw_money():
        """This Function collect User input for withdrawing money.
        
        Collects user id and password, save them to dictionary and pass it to
        the backend withdraw_money function. if the result from the backend is 
        true it restart the program. but if the result is false it call itself 
        to collect user information again.

        Return: None
        """
        print("\n")
        print(messages.account_credentials)
        u_id = pyip.inputInt("Your Id: ", greaterThan=0)
        password = pyip.inputPassword("Your Password: ")

        credentials = {"id":u_id, "password":password}
        result = BankOperationsBackend.withdraw_money(credentials)
        start_again() if result else BankOperationsUi.withdraw_money()

    @staticmethod
    def deposit_money():
        """This Function collect User input for depositing money.
        
        Collects user id and password, save them to dictionary and pass it to
        the backend deposit_money() function. if the result from the backend is 
        true it restart the program. but if the result is false it call itself 
        to collect user information again.

        Return: None
        """
        print("\n")
        print(messages.account_credentials)
        u_id = pyip.inputInt("Your Id: ", greaterThan=0)
        password = pyip.inputPassword("Your Password: ")

        credentials = {"id":u_id, "password":password}
        result = BankOperationsBackend.deposit_money(credentials)
        start_again() if result else BankOperationsUi.deposit_money()

    @staticmethod
    def check_balance():
        """This function collect user inputs for checking balnce.
             
        Collects user id and password, save them to dictionary and pass it to
        the backend check_balance() function. if the result from the backend is 
        true it restart the program. but if the result is false it call itself 
        to collect user information again.

        Return: None
        """
        print("\n")
        print(messages.check_balance)
        u_id = pyip.inputInt("Your Id: ", greaterThan=0)
        password = pyip.inputPassword("Your Password: ")

        credentials = {"id":u_id, "password":password}
        result = BankOperationsBackend.check_balance(credentials)
        start_again() if result else BankOperationsUi.check_balance()
        
    @staticmethod
    def delete_account():
        """This function collects user inputs for deleting account.
                
        Collects user id , save it to dictionary and pass it to
        the backend delete_account() function. if the result from the backend
        is true it print success message and restart the program. but if the 
        result is false it call itself to collect user information again.

        Return: None
        """
        print("\n")
        print(messages.delete_account)
        u_id = pyip.inputInt("User Id: ", greaterThan=0)

        credentials = {"id":u_id}
        result = BankOperationsBackend.delete_account(credentials)
        start_again() if result else BankOperationsUi.delete_account()


# Function outisde of the class
def start_again():
    """This function restart the program."""
    import functions
    functions.start_program()