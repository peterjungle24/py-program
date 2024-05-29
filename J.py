import pygame
import json
import tkinter
from tkinter import filedialog
from color import *
from setting import *

custom_json = open("set/custom.json")
custom = json.load(custom_json)


# main

j_mode          = custom["mode"]                            # Mode - Current
j_font          = custom["main"]["font"]                    # Font

j_cap_main      = custom["main"]["caption-main"]            # Caption - Main
j_cap_new       = custom["main"]["caption-new"]             # Caption - New

# colors

j_back_color    = custom["color"]["background-color"]       # Color - Background
j_gui_color     = custom["color"]["GUI-color"]              # Color - GUI
j_btn_color     = custom["color"]["button-color"]           # Color- Button

# texts

j_txt_title     = custom["text"]["txt-title"]               # Text - Title

# Closing file
custom_json.close()