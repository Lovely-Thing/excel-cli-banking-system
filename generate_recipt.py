import os
import sys 
import subprocess
from datetime import datetime
import fpdf

class Recipt:
    """This class contains methods for generating recipts.

    Public Methods:
    --------------
    check_balance(): -- It generate a receipt for checking balance. 
        and call the open_file() functioin to directly open the generated pdf
        reciept.
    """
    
    @staticmethod
    def check_balance(id, balance):
        """It generate a receipt for checking balance. 
        and call the open_file() functioin to directly open the generated pdf
        reciept.
        """
        recipt = fpdf.FPDF('P', 'mm', (115,93))
        recipt.add_page()
        recipt.set_font('Arial', '', 9)

        text1 = "Welcome To Banking System".center(75,"-")
        text2 = f"Client ID: {id} \n Date: {datetime.now()} \n Check Balnace \
                \n Amount: {balance} \n"
        text3 = "Thank You".center(80,"-")
        text= f"{text1} \n {text2} {text3}"

        recipt.multi_cell(100, 10, text, border=0, align='c')
        recipt.output(f"{id}-recipt.pdf")

        #open the recipt file
        run_file(f"{id}-recipt.pdf")

        
def run_file(filename):
    """Open the pdf reciept.

    It checks the operating system and based on the operating system it opens
    the pdf file.
    """
    platform = sys.platform
    if platform == "win32":
        os.startfile(filename)
    elif platform == "darwin":
        subprocess.call(["open", filename])
    else:
        # for linux
        subprocess.call(["xdg-open", filename])