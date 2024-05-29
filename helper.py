import pygame
from color import *
from text import *

def txt_adjust(surface, x = 0, y = 0):
    
    import mode
    
    mode.window.blit(surface, (x + 10, y + 10))