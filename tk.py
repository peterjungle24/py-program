import tkinter as tk
from tkinter import filedialog
from color import *
from J import *

def open_file():
    
    file_t = ("*.png", "*.jpeg")

    file = filedialog.askopenfile(mode ='r', filetypes =[("Image file", file_t)])
    
    if (file):
        
        file_img = pygame.image.load(file)
    
        import mode
    
        mode.window.fill(j_back_color)
        mode.window.blit(file_img, (255, 255))
        
    else:
        
        print("none selected. I know.")

def save_file():
    
    file_t = [("Image file", "*.png"), ("All Files", "*.*")]
    file = filedialog.asksaveasfile(filetypes = file_t, defaultextension = file_t)
    
    if (file):

        pass
    else:
        
        print("you saved nothing. Bealtyfull")