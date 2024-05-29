from tk import *
from color import *
from setting import *
from e import *
from surf import *
from text import *
from J import *
import pygame

icon = pygame.image.load(custom["main"]["icon"])
pygame.display.set_icon(icon)

fps = pygame.time.Clock()

def mode_main():

    import PYTHON_TESTS as p
    
    pygame.display.set_caption(j_cap_new)
    

    window = pygame.display.set_mode(res)
    window.fill(back_col)
    
    while True:
        
        fps.tick(60)
        
        surface()
        txt()
        ev()

        pygame.display.flip()