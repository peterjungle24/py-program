import pygame

def txt_adjust(surface, x=0, y=0):
    import program

    program.window.blit(surface, (x + 10, y + 10))

def log_info(text):
    print("{Info} " + text)


def log_error(text):
    print("{Error} " + text)


def log_init(text):
    print("{Init} " + text)