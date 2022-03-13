import pygame

from auxiliary_functions import get_font


def you_won(win, BG):
    win.blit(BG, (0, 0))
    text = get_font(50).render("YOU WON!", True, "#28a103")
    rect = text.get_rect(center=(310, 300))
    win.blit(text, rect)
    pygame.display.update()
    pygame.time.delay(2000)