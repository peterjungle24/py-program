import pygame
from color import *
from setting import *
from surf import *
from J import *
from helper import *

wi = window.get_width()
he = window.get_height()

# font
pygame.font.init()

rod = j_font

font        = pygame.font.Font(rod, 58)
font_big    = pygame.font.Font(rod, 45)
font_smol    = pygame.font.Font(rod, 35)

# render text

def txt():
    
    txt_load = font.render("load", False, black)                                # load
    txt_save = font.render("save", False, black)                              # save
    txt_credit = font.render("credit", False, black)                            # credit

    # GIT GUD
    
    txt_adjust(txt_load, 10, 10)
    txt_adjust(txt_save, 200, 10)
    #window.blit(txt_credit,   (20, 460))                                        # [ credit ] as joined to chat
    