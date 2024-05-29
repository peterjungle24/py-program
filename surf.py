import pygame, gif_pygame, sys
from color import *
from setting import *
from tk import *

window = pygame.display.set_mode(res)           # window

s_w = window.get_width()                        # entire Width screen
s_h = window.get_height()                       # entire Height screen

y = 10
x = 10

rect_gui = pygame.Rect((0, 0, s_w, 90))

# rects

rect_load = pygame.Rect((x, y, 173, 65))                    # rect [ load ]
rect_save = pygame.Rect((x + 190, y, 173, 65))            # rect [ save ]
rect_credit = pygame.Rect((x + 190 + 190, y, 173, 65))      # rect [ credit ]


def surface():
     
    # surfaces
    
    pygame.draw.rect(window, gui_col, rect_gui)                 # draw the [ rect_gui ] for store the buttons on left side.
    
    # rects

    pygame.draw.rect(window, button_col, rect_load)         # draw the [ rect_load ]
    pygame.draw.rect(window, button_col, rect_save)       # draw the [ rect_config ]
    pygame.draw.rect(window, button_col, rect_credit)       # draw the [ rect_config ]