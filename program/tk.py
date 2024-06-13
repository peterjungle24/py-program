import pygame
import helper
import sufaces
from tkinter import filedialog
from json_custom import *

pos_x = 10
pos_y = 10

def open_file():
    file_t = ("*.png", "*.jpeg")

    file = filedialog.askopenfile(mode="r", filetypes=[("Image file", file_t)])
    file_img = pygame.image.load(file)
    file_img_rect = file_img.get_rect()

    if file or file_img:

        helper.log_info("Loaded.")

        sufaces.surf_image.fill(Jcolor_img)
        sufaces.surf_image.blit(file_img, (pos_x, pos_y))

    else:

        print("none selected. I know.")

    return file_img_rect