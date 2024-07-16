import pygame
from pygame.sprite import Sprite


class Buttle(Sprite):
    def __init__(self, game):
        super().__init__()
        self.main_game = game
        self.ship = self.main_game.ship
        self.setting = self.main_game.setting
        self.screen = self.main_game.screen
        self.init_buttle()

    def init_buttle(self):
        self.rect = pygame.Rect(
            0, 0, self.setting.buttle_width, self.setting.buttle_height
        )
        self.rect.midtop = self.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.main_game.setting.buttle_speed
        self.rect.y = self.y

    def draw_buttle(self):
        pygame.draw.rect(self.screen, self.setting.buttle_color, self.rect)
