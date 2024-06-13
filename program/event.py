import pygame
import tk
from sufaces import *

def ev():
    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()

        if ev.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()

            if rect_load.collidepoint(mouse_pos) and ev.button == 1:
                tk.open_file()
                print("File loaded")

            if rect_clear.collidepoint(mouse_pos) and ev.button == 1:
                surf_image.fill(Jcolor_img)