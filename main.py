import sys, pygame, time

from components import boardFetcher
from components.Grid import Grid
from components.auxiliary_functions import format_time, get_font
from components.button import Button
from screens.game_over import game_over
from screens.loadingScreen import loading_screen
from screens.no_connection_screen import no_connection
from screens.options_menu import options_menu
from screens.winning_screen import you_won

pygame.init()

SCREEN = pygame.display.set_mode((600, 650))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

numOfLives = 3
solveSpeed = 2


def redraw_window(win, board, time, lives):
    if lives == 0:  # if we run out of lives then show game over screen
        game_over(win, BG)
        return

    win.fill((255, 255, 255))

    # Draw time
    font = pygame.font.SysFont("comicsans", 40)
    text = font.render("Time: " + format_time(time), True, (0, 0, 0))
    win.blit(text, (540 - 160, 560))

    # Draw Lives
    for i in range(lives):
        heart = pygame.image.load('assets/heart.png')
        win.blit(heart, (20 + i * 50, 560))

    # Draw grid and board
    board.draw()


def start_game(difficulty):
    win = pygame.display.set_mode((600, 650))
    pygame.display.set_caption("Sudoku")

    loading_screen(win, BG)
    requestedBoard = boardFetcher.retrieveRandomBoard(difficulty)

    if requestedBoard is None:  # if no board has been returned then there is no internet connection
        operation = no_connection(win, BG)
        if operation == "Retry":  # Try again online mode
            start_game(difficulty)
        elif operation == "Offline_Mode":  # Initiate offline mode
            play(win, boardFetcher.retrieveRandomBoard_offline(difficulty))
        return

    else:  # Initiate online mode
        play(win, requestedBoard)


def play(win, requestedBoard):
    board = Grid(9, 9, 540, 540, win, requestedBoard, solveSpeed)
    key = None
    run = True
    finishTime = -1
    start = time.time()
    lives = numOfLives
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
                    finishTime = play_time

                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                            lives -= 1
                            if lives == 0:
                                print("Game over")
                                run = False
                        key = None

                        if board.is_finished():
                            print("You won")
                            you_won(win, BG)
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key is not None:
            board.sketch(key)

        redraw_window(win, board, play_time, lives)
        pygame.display.update()


def difficulty_menu():
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Pressing escape redirect to the main menu
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    start_game("easy")
                if MEDIUM_BUTTON.checkForInput(MENU_MOUSE_POS):
                    start_game("medium")
                if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    start_game("hard")

        pygame.display.update()


def main_menu():
    global numOfLives
    global solveSpeed

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("SUDOKU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(310, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Easy Rect.png"), pos=(280, 250),
                             text_input="Play", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(300, 400),
                                text_input="Options", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Hard Rect.png"), pos=(280, 550),
                             text_input="Quit", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    difficulty_menu()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    (numOfLives, solveSpeed) = options_menu(SCREEN, BG, numOfLives, solveSpeed)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
