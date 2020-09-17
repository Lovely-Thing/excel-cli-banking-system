import bank_operations_backend
import messages
import pyinputplus as pyip

class BankOperationsUi:
    '''This class contains all the functions related to bank interface.'''

    @staticmethod
    def open_account():
        '''This account collect user inputs for opening new account'''
        print("\n")
        print(messages.open_account)
        u_id    =   pyip.inputInt("Id: ",greaterThan=0)
        name    =   pyip.inputStr("Name: ")
        address =   pyip.inputStr("Address: ")
        email   =   pyip.inputEmail("Email: ")
        balance =   pyip.inputInt("Balance: ",min=0)
        password = pyip.inputPassword("Password: ")

        user_data = [u_id,name,address,balance,email,password]
        result = bank_operations_backend.BankOperationsBackend.open_account(user_data)

        start_again() if result else BankOperationsUi.open_account()


    @staticmethod
    def withdraw_money():
        '''This Function collect User input for withdrawing money'''
        print("\n")
        print(messages.account_credentials)
        u_id        =   pyip.inputInt("Your Id: ",greaterThan=0)
        password    =   pyip.inputPassword("Your Password: ")

        credentials = {"id":u_id,"password":password}
        result = bank_operations_backend.BankOperationsBackend.withdraw_money(credentials)
        start_again() if result else BankOperationsUi.withdraw_money()


    @staticmethod
    def deposit_money():
        '''This Function collect User input for depositing money'''
        print("\n")
        print(messages.account_credentials)
        u_id        =   pyip.inputInt("Your Id: ",greaterThan=0)
        password    =   pyip.inputPassword("Your Password: ")

        credentials = {"id":u_id,"password":password}
        result = bank_operations_backend.BankOperationsBackend.deposit_money(credentials)
        start_again() if result else BankOperationsUi.deposit_money()


    @staticmethod
    def check_balance():
        '''This function collect user inputs for checking balnce.'''
        print("\n")
        print(messages.check_balance)
        u_id        =   pyip.inputInt("Your Id: ",greaterThan=0)
        password    =   pyip.inputPassword("Your Password: ")

        credentials = {"id":u_id,"password":password}
        result = bank_operations_backend.BankOperationsBackend.check_balance(credentials)
        start_again() if result else BankOperationsUi.check_balance()
    
    
    @staticmethod
    def delete_account():
        '''This function collects user inputs for deleting account'''
        print("\n")
        print(messages.delete_account)
        u_id        =   pyip.inputInt("User Id: ",greaterThan=0)

        credentials = {"id":u_id}
        result = bank_operations_backend.BankOperationsBackend.delete_account(credentials)
        start_again() if result else BankOperationsUi.delete_account()


def start_again():
    '''This function restart the program'''
    import functions
    functions.start_program()