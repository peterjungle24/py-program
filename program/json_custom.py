import json

json_custom = open("set/custom.json")   # open the file
custom = json.load(json_custom)     # load the file as JSON value.

# Main
Jmain_font = custom["main"]["font"]

# Color
Jcolor_background = custom["color"]["background"]   # background color
Jcolor_img = custom["color"]["image-background"]    # image surface background color
Jcolor_button = custom["color"]["button"]           # button color
Jcolor_gui = custom["color"]["gui"]                 # gui color

json_custom.close() # close the file