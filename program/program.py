import pygame
import setting
import event
import json_custom
import sufaces, text

pygame.init()   # initialize the pygame
pygame.font.init()  # initialize the font
pygame.joystick.init()  # initialize the joysticks. optional

window = pygame.display.set_mode(setting.res)   # create a window
fps = pygame.time.Clock()   # create a FPS clock

# while the window its open
while True:
    fps.tick(60)    # framerate
    window.fill(json_custom.Jcolor_background)  # fill the screen with the color from JSON file

    sufaces.surface()   # Surface handler
    text.txt()  # Text handler
    event.ev()  # Event handler

    pygame.display.update() # Update the screen