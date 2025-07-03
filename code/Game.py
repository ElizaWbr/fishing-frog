import sys
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Fished import Fished
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.mixer_music.load('./asset/AutumnForest.mp3')
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(-1)

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window)
                level.run()
            elif menu_return == MENU_OPTION[1]:
                fished = Fished(self.window)
                fished.run()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()  # Close Window
                quit()  # End pygame
            else:
                pygame.quit()
                sys.exit()
