import pygame
from color import *
from setting import *
from surf import *

window = pygame.display.set_mode(res)          # window

# font
pygame.font.init()

rod = "assets/Rodondo.otf"

font        = pygame.font.Font(rod, 58)
font_big    = pygame.font.Font(rod, 45)
font_smol    = pygame.font.Font(rod, 35)

# render text

def txt():

    txt_title = font_big.render("still idk what app i do", False, black)        # title. yep
    
    txt_new = font.render("new", False, black)                                  # new
    txt_load = font.render("load", False, black)                                # load
    txt_config = font.render("config", False, black)                            # config
    txt_credit = font.render("credit", False, black)                            # credit

    # GIT GUD
    
    window.blit(txt_title, (255, 560))                                          # "still idk what app i do" LMAO
    
    window.blit(txt_new,      (20, 87))                                       # [ new ] as joined to chat
    window.blit(txt_load,     (20, 175))                                      # [ load ] as joined to chat
    window.blit(txt_config,   (20, 263))                                      # [ config ] as joined to chat
    window.blit(txt_credit,   (20, 460))                                      # [ credit ] as joined to chat
    

def txt_new():
    
    txt_back = font.render("back", False, black)

    window.blit(txt_back, (15, 15))