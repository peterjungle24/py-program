import random
import pygame    as pyg
import tkinter   as tk
import sys       as sys
from J import file_choose
from setting     import *
from color       import *
from surf       import *

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

                print("load file")
                file_choose()
                
            if rect_new.collidepoint(mouse_pos) and ev.button == 1:

                print("new file")
                p.moded = "new"
                

            if rect_config.collidepoint(mouse_pos) and ev.button == 1:

                print("configurations for configure the configuration for set up the settings but settings can be configured")
                
            if rect_credit.collidepoint(mouse_pos) and ev.button == 1:

                print("made by Slugg with tutorials :)")


def ev_new():
    
    for ev in pyg.event.get():

        if ev.type == pyg.QUIT:         # if you press the X
            
            pyg.quit()                  # close
            exit()                      # close
            sys.exit()                  # close
            

        if ev.type == pyg.MOUSEBUTTONDOWN:
            
            mouse_pos = pygame.mouse.get_pos()
            import PYTHON_TESTS as p

            if Nrect_back.collidepoint(mouse_pos) and ev.button == 1:

                print("back")
                p.moded = "main"