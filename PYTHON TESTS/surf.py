import pygame, gif_pygame, sys
from color import *
from setting import *

window = pygame.display.set_mode(res)           # window

s_w = window.get_width()                        # entire Width screen
s_h = window.get_height()                       # entire Height screen

# surfaces
hs_x = 0
hs_y = 0

# rect_gui = pygame.Rect((0, 0, 205, 551))
rect_gui = pygame.Rect((0, 0, 205, window.get_height()))

# rects

rect_title = pygame.Rect((0, 550, s_w, s_h))                # rect [ title ]
rect_new = pygame.Rect((10, 77, 173, 65))                   # rect [ new ]
rect_load = pygame.Rect((10, 165, 173, 65))                 # rect [ load ]
rect_config = pygame.Rect((10, 253, 173, 65))               # rect [ config ]
rect_credit = pygame.Rect((10, 450, 173, 65))               # rect [ credit ]
    
def surface_main():
     
    # surfaces
    
    pygame.draw.rect(window, (118, 143, 165), rect_gui)             # draw the [ rect_gui ] for store the buttons on left side.
    
    # rects

    pygame.draw.rect(window, (163, 163, 163), rect_title)           # draw the [ rect_title ]
    pygame.draw.rect(window, (99, 127, 150), rect_new)              # draw the [ rect_new ]
    pygame.draw.rect(window, (99, 127, 150), rect_load)             # draw the [ rect_load ]
    pygame.draw.rect(window, (99, 127, 150), rect_config)           # draw the [ rect_config ]
    pygame.draw.rect(window, (99, 127, 150), rect_credit)           # draw the [ rect_config ]

# new mode.     ________________________________________________________________________________________________________________________________________

# [ new mode ] buttons

Nrect_back =  pygame.Rect((10, 10, 173, 65))
    
def surface_new():    
    
    pygame.draw.rect(window, (163, 163, 163), Nrect_back)