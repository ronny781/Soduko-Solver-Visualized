import sys

import pygame

from auxiliary_functions import get_font
from button import Button


def no_connection(win, BG):  # This screen rendered when there is no internet connection
    while True:
        win.blit(BG, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()

        text = get_font(45).render("No internet!", True, "#a10328")
        rect = text.get_rect(center=(310, 150))

        RETRY_BUTTON = Button(image=pygame.image.load("assets/Hard Rect.png"), pos=(280, 450),
                              text_input="Retry", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        OFFLINE_BUTTON = Button(image=pygame.image.load("assets/Medium Rect.png"), pos=(300, 300),
                                text_input="Offline Mode", font=get_font(40), base_color="#d7fcd4",
                                hovering_color="White")

        win.blit(text, rect)

        for button in [RETRY_BUTTON, OFFLINE_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETRY_BUTTON.checkForInput(MOUSE_POS):
                    return "Retry"
                if OFFLINE_BUTTON.checkForInput(MOUSE_POS):
                    return "Offline_Mode"

        pygame.display.update()
