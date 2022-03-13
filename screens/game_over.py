import pygame

from components.auxiliary_functions import get_font


def game_over(win, BG):
    win.blit(BG, (0, 0))
    text = get_font(50).render("GAME OVER", True, "#a10328")
    rect = text.get_rect(center=(310, 300))
    win.blit(text, rect)
    pygame.display.update()
    pygame.time.delay(2000)