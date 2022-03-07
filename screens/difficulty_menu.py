# import sys
#
# import pygame
#
# from auxiliary_functions import get_font
# from button import Button
# from main import play
#
#
# def difficulty_menu(SCREEN, BG):
#     while True:
#         SCREEN.blit(BG, (0, 0))
#
#         MENU_MOUSE_POS = pygame.mouse.get_pos()
#
#         MENU_TEXT = get_font(80).render("SUDOKU", True, "#b68f40")
#         MENU_RECT = MENU_TEXT.get_rect(center=(310, 100))
#
#         EASY_BUTTON = Button(image=pygame.image.load("assets/Easy Rect.png"), pos=(280, 250),
#                              text_input="Easy", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
#         MEDIUM_BUTTON = Button(image=pygame.image.load("assets/Medium Rect.png"), pos=(300, 400),
#                                text_input="Medium", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
#         HARD_BUTTON = Button(image=pygame.image.load("assets/Hard Rect.png"), pos=(280, 550),
#                              text_input="Hard", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
#
#         SCREEN.blit(MENU_TEXT, MENU_RECT)
#
#         for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
#             button.changeColor(MENU_MOUSE_POS)
#             button.update(SCREEN)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:  # Pressing escape redirect to the main menu
#                     return
#
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if EASY_BUTTON.checkForInput(MENU_MOUSE_POS):
#                     play("easy")
#                 if MEDIUM_BUTTON.checkForInput(MENU_MOUSE_POS):
#                     play("medium")
#                 if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
#                     play("hard")
#
#         pygame.display.update()