from color import *
from setting import *
from e import *
import mode
import sys, os

moded = "main"                                              # current mode

while True:
    
    if moded == "main":
    
        mode.mode_main()
    
        ex = open("logger.txt", "w")
    

    else:
    
        raise Exception(f"unknown code called [ {moded} ]")
        print(f"unknown code called [ {moded} ]")
        ex = open("logger.txt", "w")
        ex.write(f"unknown code called [ {moded} ]")
        ex.close()