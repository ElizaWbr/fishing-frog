import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, C_DARK_BLUE, FISHING_TIMEOUT_START, FISHES, WIN_WIDTH

from code.Menu import Menu


def random_fishing_timeout():
    return random.choice(FISHING_TIMEOUT_START)

def get_random_fish():
    return random.choice(FISHES)

class Level:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/GameBg.jpg').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
    def run(self):
        pygame.mixer_music.load(f'./asset/AutumnForest.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)

        fishing_start_timeout = random_fishing_timeout()
        fishing_end_timeout = 10000

        clock = pygame.time.Clock()
        allow_fishing = 0
        while True:
            clock.tick(60)
            if 0 < fishing_start_timeout < 10000:
                fishing_start_timeout -= 1
            if 0 < fishing_end_timeout < 10000:
                fishing_end_timeout -= 1

            if fishing_start_timeout == 0:
                fishing_end_timeout = 120
                fishing_start_timeout = 10000

                self.level_text(25, "SPACE TO FISH", C_WHITE, ((WIN_WIDTH / 2), 200))
                allow_fishing = 1

            if fishing_end_timeout == 0:
                fishing_start_timeout = random_fishing_timeout()
                fishing_end_timeout = 10000

                self.window.blit(source=self.surf, dest=self.rect)
                allow_fishing = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if allow_fishing == 1:

                            fish = get_random_fish()
                            self.level_text(40, fish, C_DARK_BLUE, ((WIN_WIDTH / 2), 300))

                            fish_surf = pygame.image.load('./asset/fishes/' + fish + '.png').convert_alpha()
                            fish_rect = fish_surf.get_rect(center=((WIN_WIDTH / 2), 400))

                            self.window.blit(source=fish_surf, dest=fish_rect)

                            allow_fishing = 0
                            fishing_end_timeout = 120
                            fishing_start_timeout = 10000
                    if event.key == pygame.K_BACKSPACE:
                        menu = Menu(self.window)
                        menu.run()

            if 0 <= fishing_start_timeout < 10000:
                self.window.blit(source=self.surf, dest=self.rect)
                self.level_text(30, f'Next fish in {fishing_start_timeout / 60:.0f}s', C_WHITE, ((WIN_WIDTH / 2), 70))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
