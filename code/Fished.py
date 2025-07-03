import sys
import pygame

from pygame import Surface, Rect, KEYDOWN, K_BACKSPACE
from pygame.font import Font

from code.Const import C_DARK_BLUE, C_WHITE, WIN_WIDTH
from code.DBProxy import DBProxy

class Fished:
    def __init__(self, window: Surface):
        self.name = ""
        self.window = window
        self.surf = pygame.image.load('./asset/GameBg.jpg').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, name: str):
        self.name = name
        db_proxy = DBProxy('DBFishes')
        db_proxy.save(name)
        db_proxy.close()

    def run(self):
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(20, 'IMAGE          NAME          FISHED', C_DARK_BLUE, (WIN_WIDTH / 2, 60))

        db_proxy = DBProxy('DBFishes')
        list_fishes = db_proxy.retrieve_all_fishes()
        db_proxy.close()
        height = 70

        for current_fish in list_fishes:
            fish_id, name, fished = current_fish
            height = height + 55

            fish_surf = pygame.image.load('./asset/fishes/' + name + '.png').convert_alpha()
            fish_rect = fish_surf.get_rect(center=(90, height))
            self.window.blit(source=fish_surf, dest=fish_rect)

            self.score_text(20, f'          {name}          {fished}', C_DARK_BLUE,(WIN_WIDTH / 2, height))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
