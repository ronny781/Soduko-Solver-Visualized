import pygame

def format_time(secs):
    sec = secs % 60
    minute = secs // 60
    hour = minute // 60

    secString = str(sec)
    if sec < 10:
        secString = "0" + secString

    mat = " " + str(minute) + ":" + secString
    return mat


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)