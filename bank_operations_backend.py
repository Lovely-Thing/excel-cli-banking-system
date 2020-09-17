from connections import bank_data,rows,cols,sheet,columns
import messages
import pyinputplus as pyip
import generate_recipt


class BankOperationsBackend:
    '''This Class is contain all the funtionalities which add, read, delete, withdraw, depsoit.'''

    @staticmethod
    def open_account(data):
        global rows
        global cols
        '''This function add user data to excel file'''
        are_unique = BankOperationsBackend.check_email_id_existance(data[0],data[4])
        if not are_unique:
            return False

        for turn in range(1,cols+1):
            sheet.cell(row=rows+1,column=turn,value=data[turn-1])
            bank_data.save("bank_data.xlsx")

        # update rows and cols, and sheet 
        rows = bank_data.active.max_row
        cols = bank_data.active.max_column

        print(messages.account_success)
        print("\n")
        return True


    @staticmethod
    def check_email_id_existance(uid,email):
        '''This function ensure the email to be unique in the database'''
        for row in range(1,rows+1):
            # id is stored at column one of every row and value is stored at column 5
            db_id_value = sheet.cell(row=row,column=columns['ID']).value
            db_email_value = sheet.cell(row=row,column=columns['Email']).value
            if uid == db_id_value:
                print(messages.id_not_unique)
                return False
            elif email == db_email_value:
                print(messages.email_not_unique)
                return False
        return True


    @staticmethod
    def withdraw_money(data):
        '''This function withdraw money from user account.'''
        
        credential_result = BankOperationsBackend.check_credetials(data) 
        if not credential_result:
            print(messages.invalid_credentials)
            return False
        
        balance_validity_update = BankOperationsBackend.check_balance_and_update(credential_result)
        if not balance_validity_update:
            return False

        return True


    @staticmethod
    def check_balance_and_update(balance_cell):
        status = True
        '''This function return true if the user have enough balance and update it or return false.'''
        if balance_cell.value <=0:
            print(messages.not_enough_balance)
            status = False
            return status

        try_count = 0
        while status:
            if try_count > 3:
                return False

            print("\n")
            withdraw_amount = pyip.inputInt("Amount of money you want to withdraw: ",greaterThan=0)
            if withdraw_amount > balance_cell.value:
                print(messages.not_enough_balance + f". Your Ballance is: {balance_cell.value}")
                try_count +=1
            else:
                balance_cell.value = balance_cell.value - withdraw_amount
                bank_data.save("bank_data.xlsx")
                print(messages.withdraw_deposit_success.format("Withdrawed",balance_cell.value))
                print("\n")
                status = True
                break

        return status


    @staticmethod
    def deposit_money(data):
        '''This funcction deposit money to user bank account'''
        balance_cell = BankOperationsBackend.check_credetials(data) 
        if not balance_cell:
            print(messages.invalid_credentials)
            return False
        
        print("\n")
        deposit_amount = pyip.inputInt("Amount of money you want to deposit: ",greaterThan=0)
        balance_cell.value = balance_cell.value + deposit_amount
        bank_data.save("bank_data.xlsx")
        print(messages.withdraw_deposit_success.format("Desposited",balance_cell.value))
        print("\n")
        return True

    
    @staticmethod
    def check_balance(data):
        '''This function check user balance'''
        balance_cell = BankOperationsBackend.check_credetials(data)
        if not balance_cell:
            print(messages.invalid_credentials)
            return False

        print("\n")
        generate_recipt.Recipt.check_balance(data['id'],balance_cell.value)
        
        print(messages.balance_result.format(balance_cell.value))
        print("\n")
        return True


    @staticmethod
    def delete_account(data):
        '''This function delete user account'''
        global rows
        global cols
        for row in range(2,rows+1):
            db_id_value = sheet.cell(row=row,column=columns["ID"]).value
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
    def check_credetials(data):
        '''This function check if the id and password entered by the user is in db or not'''
        for row in range(2,rows+1):
            db_id_value = sheet.cell(row=row,column=columns["ID"]).value
            db_pass_value = sheet.cell(row=row,column=columns["Password"]).value
            if data['id'] == db_id_value and data['password'] == db_pass_value:
                # user_data = {}
                return sheet.cell(row=row,column=columns['Balance']) #return balance cell
        return False
