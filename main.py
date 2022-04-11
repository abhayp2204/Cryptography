# General imports
import colorama
from colorama import Fore, Back, Style
import os

# Local imports
from input import *
from util import *
from controls import *
from ciphers import *

# Setup
colorama.init(autoreset=True)

# Data
stars = "*"*10
space = " "*2
ciphers = [
    "Caesar Cipher",
    "Monoalphebatic Cipher",
    "Hill Cipher"]

def select_cipher(arrow):
    while(True):
        key = input_to(Get())
        if key == "q":
            exit()
        if key == "c":
            print()
            return arrow
        
        arrow += (key == " ")
        arrow %= len(ciphers)
        os.system("clear")
        
        # print(Fore.CYAN + stars + space + "CRYPTOGRAPHY" + space + stars)
        starprint(Fore.CYAN, 10, 2, "CRYPTOGRAPHY")
        i = 0
        for cipher in ciphers:
            selection = "> " if i == arrow else "  "
            print(Fore.YELLOW + selection + cipher)
            i += 1
   
def get_plain_text():
    return input("Plain text: ")
   
arrow = select_cipher(0)

# Call cipher function
if arrow == 0:
    caesar_cipher()
elif arrow == 1:
    monoalphebatic_cipher()
elif arrow == 2:
    hill_cipher()