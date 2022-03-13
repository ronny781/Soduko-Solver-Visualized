import pygame

from auxiliary_functions import get_font


def loading_screen(win, BG):
    win.blit(BG, (0, 0))
    text = get_font(50).render("Loading...", True, "#b68f40")
    rect = text.get_rect(center=(310, 300))
    win.blit(text, rect)
    pygame.display.update()
