import sys

import pygame

from auxiliary_functions import get_font
from button import Button


def options_menu(SCREEN, BG, numOfLives, solveSpeed):
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("OPTIONS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(310, 100))

        LIVES_BUTTON = Button(image=pygame.image.load("assets/big-heart.png"), pos=(200, 250),
                              text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        font = get_font(75)
        text = font.render(":{}".format(numOfLives), True, (255, 255, 255))
        SCREEN.blit(text, (280, 210))

        UP_BUTTON1 = Button(image=pygame.image.load("assets/arrow up.png"), pos=(500, 220),
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        DOWN_BUTTON1 = Button(image=pygame.image.load("assets/arrow down.png"), pos=(500, 280),
                              text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SPEED_TEXT = get_font(30).render("Solve Speed:{}".format(solveSpeed), True, "#ffffff")
        SPEED_RECT = SPEED_TEXT.get_rect(center=(240, 380))

        UP_BUTTON2 = Button(image=pygame.image.load("assets/arrow up.png"), pos=(500, 350),
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        DOWN_BUTTON2 =Button(image=pygame.image.load("assets/arrow down.png"), pos=(500, 410),
                              text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(SPEED_TEXT, SPEED_RECT)
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [LIVES_BUTTON, UP_BUTTON1, DOWN_BUTTON1, UP_BUTTON2, DOWN_BUTTON2]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if UP_BUTTON1.checkForInput(MENU_MOUSE_POS):
                    if numOfLives < 7:
                        numOfLives += 1
                        LIVES_BUTTON.update(SCREEN)
                if DOWN_BUTTON1.checkForInput(MENU_MOUSE_POS):
                    if numOfLives > 1:
                        numOfLives -= 1
                        LIVES_BUTTON.update(SCREEN)
                if UP_BUTTON2.checkForInput(MENU_MOUSE_POS):
                    if solveSpeed < 5:
                        solveSpeed += 1

                if DOWN_BUTTON2.checkForInput(MENU_MOUSE_POS):
                    if solveSpeed > 1:
                        solveSpeed -= 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Pressing escape redirect to the main menu
                    return numOfLives, solveSpeed
            #     if event.key == pygame.K_UP:  # Pressing escape redirect to the main menu
            #         if numOfLives < 7:
            #             numOfLives += 1
            #             LIVES_BUTTON.update(SCREEN)
            #     if event.key == pygame.K_DOWN:  # Pressing escape redirect to the main menu
            #         if numOfLives > 1:
            #             numOfLives -= 1
            #             LIVES_BUTTON.update(SCREEN)

        pygame.display.update()
