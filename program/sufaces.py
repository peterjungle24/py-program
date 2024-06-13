import pygame
import colors
import tk
import setting
from json_custom import *

# arguments: pygame.Rect(x, y, width, heigth)
# arguments: pygame.draw.rect(surface, (x, y))

window = pygame.display.set_mode(setting.res)  # window

s_w = window.get_width()  # entire Width screen
s_h = window.get_height()  # entire Height screen

x = 10  # x
y = 10  # y

# -------------------------
# surfaces
# -------------------------

surf_image = pygame.Surface((500, 500))
surf_image.fill(Jcolor_img)

rect_image = surf_image.get_rect()

# -------------------------
# rects
# -------------------------

rect_gui = pygame.Rect((0, 0, s_w, 90))

rect_load = pygame.Rect((x, y, 173, 65))  # rect [ load ]
rect_save = pygame.Rect((200, y, 173, 65))  # rect [ save ]
rect_credit = pygame.Rect((200 + 190, y, 173, 65))  # rect [ credit ]
rect_clear = pygame.Rect((790, 120, 173, 65))  # rect [ clear ]
rect_tag = pygame.Rect((790, 200, 173, 65))  # rect [ tag ]


def surface():
    # -------------------------
    # surfaces
    # -------------------------

    window.blit(surf_image, (250, 120))

    # -------------------------
    # rects
    # -------------------------

    pygame.draw.rect(window, Jcolor_gui, rect_gui)  # draw the [ rect_gui ] for store the buttons on upper side.

    pygame.draw.rect(window, Jcolor_button, rect_load)  # draw the [ rect_load ]
    pygame.draw.rect(window, Jcolor_button, rect_save)  # draw the [ rect_save ]
    pygame.draw.rect(window, Jcolor_button, rect_credit)  # draw the [ rect_credit ]
    pygame.draw.rect(window, Jcolor_button, rect_clear)  # draw the [ rect_clear ]
    pygame.draw.rect(window, Jcolor_button, rect_tag)  # draw the [ rect_tag ]