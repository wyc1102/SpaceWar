import pygame
import sys
from setting import Setting
from ship import Ship
from buttle import Buttle
from pygame.sprite import Group
from enemy import Enemy
from button import Button
from score_board import ScoreBoard


class Main_game:
    def __init__(self):
        pygame.init()
        self.setting = Setting()
        self.clock = pygame.time.Clock()
        self.enemies = Group()
        self.init_game()
        self.ship = Ship(self)
        self.buttles = Group()

    def init_game(self):
        self.screen = pygame.display.set_mode(self.setting.screen_size)
        self.screen_rect = self.screen.get_rect()
        self.game_active = False
        self.score = 0.0
        self.life = self.setting.ship_life_max

    def run(self):
        while True:

            self.check_event()
            if self.game_active:
                self.check_collide()
                self.screen_update()
            else:
                self.screen.fill(self.setting.bg_color)
                self.screen.blit(self.ship.image, self.ship.rect)
                self.enemies.draw(self.screen)
                self.draw_button()
                pygame.display.flip()
            self.clock.tick(60)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.check_event_down(event)
            self.check_event_up(event)
            self.check_play_button(event)

    def screen_update(self):
        self.ship.update()
        self.buttles.update()
        self.enemies.update()

        self.create_enemy()
        self.remove_buttle()
        self.remove_enemy()

        self.screen.fill(self.setting.bg_color)
        for buttle in self.buttles:
            buttle.draw_buttle()
        self.ship.draw_ship()
        self.enemies.draw(self.screen)
        self.score_board = ScoreBoard(self)
        self.score_board.draw_score_board()

        pygame.display.flip()

    def check_event_down(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.ship.move_up = True
            if event.key == pygame.K_DOWN:
                self.ship.move_down = True
            if event.key == pygame.K_LEFT:
                self.ship.move_left = True
            if event.key == pygame.K_RIGHT:
                self.ship.move_right = True
            if event.key == pygame.K_SPACE:
                self.add_buttle()

    def check_event_up(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.ship.move_up = False
            if event.key == pygame.K_DOWN:
                self.ship.move_down = False
            if event.key == pygame.K_LEFT:
                self.ship.move_left = False
            if event.key == pygame.K_RIGHT:
                self.ship.move_right = False

    def add_buttle(self):
        if self.buttles.__len__() < self.setting.buttle_max_number:
            new_buttle = Buttle(self)
            self.buttles.add(new_buttle)

    def add_enemy(self):
        new_enemy = Enemy(self)
        self.enemies.add(new_enemy)

    def remove_buttle(self):
        for buttle in self.buttles.copy():
            if buttle.rect.bottom < 0:
                self.buttles.remove(buttle)

    def remove_enemy(self):
        for enemy in self.enemies.copy():
            if enemy.rect.top > self.screen_rect.bottom:
                self.enemies.remove(enemy)

    def create_enemy(self):
        enemy_example = Enemy(self)
        enemy_height = enemy_example.rect.height
        if self.enemies.sprites().__len__() <= 0:
            self.add_enemy()
        elif (
            self.enemies.sprites()[-1].rect.top
            > enemy_height * self.setting.enemy_create_probability
        ):
            self.add_enemy()

    def check_collide(self):
        self.buttle_enemy_collide()
        self.ship_enemy_collide()

    def buttle_enemy_collide(self):
        collision = pygame.sprite.groupcollide(self.buttles, self.enemies, True, True)
        if collision:
            self.score += self.setting.enemy_score_add

    def draw_button(self):
        self.play_button = Button(self, "play")
        self.play_button.draw_button()

    def check_play_button(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.game_active:
                if self.play_button.rect.collidepoint(pygame.mouse.get_pos()):
                    self.restart()
                    self.game_active = True

    def restart(self):
        self.buttles.empty()
        self.enemies.empty()
        self.ship.x = self.ship.start_x
        self.ship.y = self.ship.start_y
        self.life = self.setting.ship_life_max
        self.score = 0.0

    def ship_enemy_collide(self):
        collision = pygame.sprite.spritecollide(self.ship, self.enemies, True)
        if collision:
            pygame.time.wait(500)
            if self.life > 1:
                self.lost_one_life()
            else:
                self.life -= 1
                self.game_active = False

    def lost_one_life(self):
        self.life -= 1
        self.buttles.empty()
        self.enemies.empty()
        self.ship.x = self.ship.start_x
        self.ship.y = self.ship.start_y


main_game = Main_game()
main_game.run()
