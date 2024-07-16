from pygame.sprite import Sprite
import pygame
import random


class Enemy(Sprite):
    def __init__(self, main_game):
        super().__init__()
        self.main_game = main_game
        self.screen = self.main_game.screen
        self.screen_rect = self.main_game.screen_rect
        self.setting = self.main_game.setting
        self.init_enemy()

    def init_enemy(self):
        self.image = pygame.image.load("img/alien.bmp")
        self.image = pygame.transform.scale(self.image, self.setting.enemy_size)
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.rect.x = random.randint(
            self.width, self.screen_rect.right - self.width * 2
        )
        self.rect.y = -self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.direction = self.random_direction()

    def random_direction(self):
        if random.random() > 0.5:
            return 1
        else:
            return -1

    def update(self):
        self.change_direction()
        self.y += self.setting.enemy_down_speed
        self.x += self.setting.enemy_row_speed * self.direction
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_enemy(self):
        self.screen.blit(self.image, self.rect)

    def check_row_edge(self):
        if self.rect.left < 0 or self.rect.right > self.screen_rect.right:
            return True
        else:
            return False

    def check_down_edge(self):
        if self.rect.y > self.screen_rect.bottom:
            return True
        else:
            return False

    def change_direction(self):
        if self.check_row_edge():
            self.direction *= -1
        elif self.random_unit(self.setting.enemy_change_direction_probability):
            pass
        else:
            self.direction *= -1

    def random_unit(self, p):
        assert p >= 0 and p <= 1, "概率P的值应该处在[0,1]之间！"
        if p == 0:  # 概率为0，直接返回False
            return False
        if p == 1:  # 概率为1，直接返回True
            return True
        p_digits = len(str(p).split(".")[1])
        interval_begin = 1
        interval__end = pow(10, p_digits)
        R = random.randint(interval_begin, interval__end)
        if float(R) / interval__end < p:
            return True
        else:
            return False
