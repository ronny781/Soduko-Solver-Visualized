import pygame

from auxiliary_functions import get_font


def game_over(win, BG):
    win.blit(BG, (0, 0))
    MENU_TEXT = get_font(50).render("GAME OVER", True, "#a10328")
    MENU_RECT = MENU_TEXT.get_rect(center=(310, 300))
    win.blit(MENU_TEXT, MENU_RECT)
    pygame.display.update()
    pygame.time.delay(2000)