import sys


from Grid import Grid
from button import Button

import pygame
import time


pygame.font.init()
pygame.init()

SCREEN = pygame.display.set_mode((600, 650))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def redraw_window(win, board, time, strikes):
    win.fill((255, 255, 255))
    # Draw time
    fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render("Time: " + format_time(time), True, (0, 0, 0))
    win.blit(text, (540 - 160, 560))
    # Draw Strikes
    text = fnt.render("X " * strikes, True, (255, 0, 0))
    win.blit(text, (20, 560))
    # Draw grid and board
    board.draw()


def format_time(secs):
    sec = secs % 60
    minute = secs // 60
    hour = minute // 60

    mat = " " + str(minute) + ":" + str(sec)
    return mat


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play(difficulty):
    win = pygame.display.set_mode((600, 650))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540, win, difficulty)
    key = None
    run = True
    finishTime = -1
    start = time.time()
    strikes = 0
    while run:

        play_time = finishTime if finishTime != -1 else round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_KP1:
                    key = 1
                if event.key == pygame.K_KP2:
                    key = 2
                if event.key == pygame.K_KP3:
                    key = 3
                if event.key == pygame.K_KP4:
                    key = 4
                if event.key == pygame.K_KP5:
                    key = 5
                if event.key == pygame.K_KP6:
                    key = 6
                if event.key == pygame.K_KP7:
                    key = 7
                if event.key == pygame.K_KP8:
                    key = 8
                if event.key == pygame.K_KP9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None

                if event.key == pygame.K_SPACE:
                    board.solve_gui()
                    finishTime = play_time;

                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                            strikes += 1
                        key = None

                        if board.is_finished():
                            print("Game over")

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key is not None:
            board.sketch(key)

        redraw_window(win, board, play_time, strikes)
        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("SUDOKU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(310, 100))

        EASY_BUTTON = Button(image=pygame.image.load("assets/Easy Rect.png"), pos=(280, 250),
                             text_input="Easy", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        MEDIUM_BUTTON = Button(image=pygame.image.load("assets/Medium Rect.png"), pos=(300, 400),
                               text_input="Medium", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        HARD_BUTTON = Button(image=pygame.image.load("assets/Hard Rect.png"), pos=(280, 550),
                             text_input="Hard", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play("easy")
                if MEDIUM_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play("medium")
                if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play("hard")

        pygame.display.update()


main_menu()
