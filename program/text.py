import helper
import pygame
from colors import *
from setting import *
from sufaces import *
from json_custom import *

window = pygame.display.set_mode(res)

wi = window.get_width()
he = window.get_height()

# font
pygame.font.init()  # initialize the font

rod = Jmain_font  # file from the font

font = pygame.font.Font(rod, 58)  # font
font_big = pygame.font.Font(rod, 45)  # big font
font_smol = pygame.font.Font(rod, 35)  # smol font


# render text

def txt():
    txt_load = font.render("Load", False, black)  # load
    txt_save = font.render("Save", False, black)  # save
    txt_credit = font.render("Credit", False, black)  # credit
    txt_clear = font.render("Clear", False, black)  # clear

    # GIT GUD

    helper.txt_adjust(txt_load, 10, 10)  # adjust the text and add the [ LOAD ]
    helper.txt_adjust(txt_save, 200, 10)  # adjust the text and add the [ SAVE ]
    helper.txt_adjust(txt_credit, 390, 10)  # adjust the text and add the [ CREDIT ]
    helper.txt_adjust(txt_clear, 790, 120)