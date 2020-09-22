import re
import pyinputplus as pyip
import messages
from generate_recipt import Recipt
from connections import bank_data, rows, cols, sheet, columns


class BankOperationsBackend:
    """This class contains all backend operations related to bank.

    Public Methods:
    --------------
    open_account(data): -- creates new account if email and id are unique.
    withdraw_mondey(data): -- withdraw money from user account
    deposit_money(data): -- deposit money to account
    check_balance(data): -- check balance and call the generate recipt method
    delete_account(data): -- delete user account based on ID

    Private Methods:
    ---------------
    __check_email_id_existance(uid, email): -- 
        Return True if email and id are unique.
    __check_credentials(data): -- return false if fail else return balance cell
    __check_balance_and_update(balance_cell): -- 
        Check the sufficiency of the balance and update the balance cell
    """

    @staticmethod
    def open_account(data):
        """This function add new user account to database
        
        Create New user and also update the excel file max rows and columns.

        Parameter:
        ---------
        data: list -- New user data to be added to database

        Return: boolean
        ---------------
        False: if the user email and id already exists in database.
        True: if user recored added seccessfully.
        """
        global rows
        global cols
        are_unique = BankOperationsBackend.__check_email_id_existance(
            data[0], data[4])
        if not are_unique:
            return False

        for turn in range(1, cols+1):
            sheet.cell(row=rows+1, column=turn, value=data[turn-1])
            bank_data.save("bank_data.xlsx")

        # update rows and cols
        rows = bank_data.active.max_row
        cols = bank_data.active.max_column

        print(messages.account_success)
        print("\n")
        return True

    @staticmethod
    def __check_email_id_existance(uid, email):
        """This private function ensure the email to be unique in the database
        
        Parameters:
        -----------
        uid: int -- user entered id to be checked in database
        email: string -- user entered email to be checked in database 

        Return: boolean
        ---------------
        False: If email or Id already exists in datbase
        True: If email and Id are not in database
        """

        for row in range(1, rows+1):
            db_id_value = sheet.cell(row=row, column=columns['ID']).value
            db_email_value = sheet.cell(row=row, column=columns['Email']).value
            
            if uid == db_id_value:
                print(messages.id_not_unique)
                return False
            elif email == db_email_value:
                print(messages.email_not_unique)
                return False
        return True

    @staticmethod
    def withdraw_money(data):
        """This function withdraw money from user account.
        
        It calls two more functions to check the credential and if the its true
        then it call the private __check_balance_and_update function to check 
        the sufficiency of balance and update the balance.

        parameters:
        -----------
        data: Dictionary -- contain user entered id and password

        Return: boolean
        ---------------
        False: If the credentials are wrong compared to database, or if the 
            balance is insufficient to be withdrawed.
        True: If credentials are corrct, the ballance is sufficient and the
            balalance is upadated seccessfully.
        """
        
        credential_result = BankOperationsBackend.__check_credetials(data) 
        if not credential_result:
            print(messages.invalid_credentials)
            return False
        
        balance_update = BankOperationsBackend.__check_balance_and_update(
            credential_result)
        
        if not balance_update:
            return False

        return True

    @staticmethod
    def __check_balance_and_update(balance_cell):
        """This function check balance sufficiency and update the balance

        This function is called from the withdraw_money() function and it make
        sure that the account has sufficient balance to be withdrawe. and if it
        is true then it withdraw the money. If the user typed wrong amount 3 
        times then user will be asked to enter id and password again.

        parmeters:
        ---------
        balance_cell: object cell -- the object of balance_cell passed from the 
            withdraw_money() function. We can access its value by .value property
        
        Return: boolean
        ---------------
        False: If user has 0 money, if user enter insufficient amount 3 times.
        True: if the balnce cell is updated seccessfully.
        """
        status = True
        if balance_cell.value <=0:
            print(messages.not_enough_balance)
            status = False
            return status

        try_count = 0
        while status:
            if try_count > 3:
                return False

            print("\n")
            withdraw_amount = pyip.inputInt(
                "Amount of money you want to withdraw: ", greaterThan=0)

            if withdraw_amount > balance_cell.value:
                print(messages.not_enough_balance 
                   + f". Your Ballance is: {balance_cell.value}")
                try_count += 1
            else:
                balance_cell.value = balance_cell.value - withdraw_amount
                bank_data.save("bank_data.xlsx")
                print(messages.withdraw_deposit_success.format("Withdrawed" 
                    , balance_cell.value))
                print("\n")
                status = True
                break

        return status

    @staticmethod
    def deposit_money(data):
        """This funcction deposit money to user bank account.

        First it calls the check credential method to make sure the user is 
        correct one, if user is correct it then adds the new depsoit amount 
        to the balance cell value returned by the _check_credenctial function
        and finnaly save the file.
 
        Parameters:
        -----------
        data: Dictionary -- contain user entered id and password.

        Return: boolean
        ---------------
        False: if the credential is wrong .
        True: if the depsiting is done seccessfully.
        """
        balance_cell = BankOperationsBackend.__check_credetials(data) 
        if not balance_cell:
            print(messages.invalid_credentials)
            return False
        
        print("\n")
        deposit_amount = pyip.inputInt("Amount of money you want to deposit: "
            , greaterThan=0)
        balance_cell.value = balance_cell.value + deposit_amount
        bank_data.save("bank_data.xlsx")
        print(messages.withdraw_deposit_success.format("Desposited"
            , balance_cell.value))
        print("\n")
        return True
    
    @staticmethod
    def check_balance(data):
        """This function check user balance.

        It first check user balance and print the result in console beside that
        it also call check_balance() method from generate_recipt module to 
        also generate a recipt for the cheking balance.

        Parameters:
        ----------
        data: Dictionary -- contain user entered id and password.

        Return: boolean
        --------------
        False: if the credential is wrong, or if any errors happen during 
            generating the receipt from generate_recipt module.
        True: if credential is correct and receipt is seccessfully generated.
        
        """
        balance_cell = BankOperationsBackend.__check_credetials(data)
        
        if not balance_cell:
            print(messages.invalid_credentials)
            return False

        print("\n")
        Recipt.check_balance(data['id'], balance_cell.value)
        
        print(messages.balance_result.format(balance_cell.value))
        print("\n")
        return True

    @staticmethod
    def delete_account(data):
        """This function delete user account.
        
        This function does not ask for passwrod ony takes the id and delete the
        account if it is in the database.and finnaly it updated the max_rows and
        max_columns number. And save  file in  end.

        Parameters:
        ----------
        data: Dictionary -- contain user id to be deleted

        Return: boolean
        ---------------
        False: if id is not found 
        True: if id is found and recored id deleted
        """
        global rows
        global cols
        for row in range(2, rows+1):
            db_id_value = sheet.cell(row=row, column=columns["ID"]).value
            if data['id'] == db_id_value:
                sheet.delete_rows(row)
                bank_data.save("bank_data.xlsx")
                # update rows and cols, and sheet 
                rows = bank_data.active.max_row
                cols = bank_data.active.max_column
                print(messages.account_deleted_success)
                print("\n")
                return True

        print(messages.id_not_found)
        return False

    @staticmethod
    def __check_credetials(data):
        """This function check if the id and passwrod exists in db or not

        It loops through every row's id and password column and check it 
        with the user entered id and password.

        Parameters:
        ----------
        data: Dictionary -- contains user entered id and password.

        Return:
        -------
        False: if the id and password does not match the database.
        balnce_cell: if the credentials matches the database.
        """
        for row in range(2, rows+1):
            db_id_value = sheet.cell(row=row, column=columns["ID"]).value
            db_pass_value = sheet.cell(row=row, 
                column=columns["Password"]).value
            if data['id'] == db_id_value and data['password'] == db_pass_value:
                #return balance cell
                return sheet.cell(row=row, column=columns['Balance']) 
        return False

