# netlinks-banking_system
This is a  simple CLI banking application built with python 3.8. wich is able to:
1. Open New Client Account
  - Client account informations are stored in xlsx file.
  - Client Informations includs (ID unique,Name,Address,Email unique,balance,password)
  
2. Client can withdraw money
  - First he/she must authenticate to system using ID and Password
  - After withdrawing the the client balance changes to new value

3. Client Deposit Money

4. Check Clients Balance using ID
   - After checking the balance a recipt (bill) will be generated and automatically opend to show user balance information 
5. Delete Clients Account Based on ID

6. Quit the program

# Prerequisites Modules To Install
This project uses the follwing external modules to be installed before running the project:
- openpyxl: A module used to read and write the excel files. [How to Install?](https://openpyxl.readthedocs.io/en/stable/)
- pyinputplus: A module used to validate user inputs to the system. [How to Install?](https://pypi.org/project/PyInputPlus/)
- fpdf: A module used for working with pdf files. [How to Install](https://pypi.org/project/fpdf/)
# Structure of project
This project consist of 6 python files and one excel file.
  1. main.py: This is the starting point of the project. **_We must run the project from main.py_**. This File is calling the function to start the project.
  2. functions.py: This file contain functions related to project. Like  starting the project, checking user choice.
  3. bank_operations_ui: This file consist of one class which has methods to take user inputs for deffrent opperations, like adding,withdrawing, depositing, deleting and etc...
  4. bank_operations_backend: This File consist of one class which has which has methods to work with the backend (files in this case). This class methods are are called from the bank_operations_ui file.
  5. generate_recipt.py:This file contain a class with has methods for creating recipts (for now it only generate for the chacking balance). And also it has a function with opens the generated recipts after they have been created.
  6. messages.py: containe all messages to be printed in the system
  
# How to run the project:
- install modules mentioned above
- open the main.py file and run the project
  - If the excel file does not exists then it creates one and you need to restart the program
- after running the project you will be asked to run an operations (adding user, withdrawing money, depositing money, deleting user, cheking balance)
