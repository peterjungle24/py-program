import random
import pygame    as pyg
import tkinter
import sys       as sys
from setting     import *
from color       import *
from surf import *
from tk import *

window = pyg.display.set_mode(res)

def ev():
    
    for ev in pyg.event.get():

        if ev.type == pyg.QUIT:         # if you press the X
            
            pyg.quit()                  # close
            exit()                      # close
            sys.exit()                  # close
            

        if ev.type == pyg.MOUSEBUTTONDOWN:
            
            mouse_pos = pygame.mouse.get_pos()
            import PYTHON_TESTS as p

            if rect_load.collidepoint(mouse_pos) and ev.button == 1:

                print("load image")
                open_file()

            if rect_save.collidepoint(mouse_pos) and ev.button == 1:

                print("saved file.")
                save_file()
                
            if rect_credit.collidepoint(mouse_pos) and ev.button == 1:

                print("made by Slugg with tutorials :)")