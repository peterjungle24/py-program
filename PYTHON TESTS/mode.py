from color import *
from setting import *
from e import *
from surf import *
from text import *
import pygame

def mode_main():

    import PYTHON_TESTS as p

    pygame.init()                                  # initializes the init for initizalize

    window = pygame.display.set_mode(res)          # window
    pygame.display.set_caption("Main")
    window.fill(cyan)                           # fill window with Cyan color

    while True:                                     # while run the program

        surface_main()                              # add surface
        txt()                                       # add text
        ev()                                        # add event handler

        if p.moded == "new":
            window.fill(cyan)
            mode_new()

        pygame.display.flip()

def mode_new():
    
    import PYTHON_TESTS as p
    
    pygame.display.set_caption("New")
    window = pygame.display.set_mode(res)
    window.fill(cyan)
    
    while True:
        
        surface_new()
        txt_new()
        ev_new()
        
        if p.moded == "main":
            window.fill(cyan)
            mode_main()

        pygame.display.flip()