from color import *
from setting import *
from e import *
import mode
import sys, os
from J import *

moded = j_mode                  # current mode
running = True

while running:
    
    if moded == "main":
    
        mode.mode_main()
    
        ex = open("logger.txt", "w")
        ex.write("")
    
    else:
    
        raise Exception(f"unknown code called [ {moded} ]")
        print(f"unknown code called [ {moded} ]")
        ex = open("logger.txt", "w")
        ex.write(f"unknown code called [ {moded} ]")
        ex.close()

        running = False