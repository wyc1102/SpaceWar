import pygame
import setting


class Ship:
    def __init__(self, main_game):
        self.main = main_game
        self.screen = self.main.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = main_game.setting
        self.init_ship()

    def init_ship(self):
        self.image = pygame.image.load("img/ship.bmp")
        self.image = pygame.transform.scale(self.image, self.setting.ship_size)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.start_x = self.x
        self.start_y = self.y
        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

    def update(self):
        if self.move_up and self.rect.top > 0:
            self.y -= self.setting.ship_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.ship_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_ship(self):
        self.screen.blit(self.image, self.rect)


class Testgame:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((1020, 690))
        self.setting = setting.Setting()


if __name__ == "__main__":
    testgame = Testgame()
    a = Ship(testgame)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    a.move_up = True
                if event.key == pygame.K_DOWN:
                    a.move_down = True
                if event.key == pygame.K_LEFT:
                    a.move_left = True
                if event.key == pygame.K_RIGHT:
                    a.move_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    a.move_up = False
                if event.key == pygame.K_DOWN:
                    a.move_down = False
                if event.key == pygame.K_LEFT:
                    a.move_left = False
                if event.key == pygame.K_RIGHT:
                    a.move_right = False
        a.update()
        testgame.screen.fill((255, 255, 255))
        testgame.screen.blit(a.image, a.rect)
        pygame.display.flip()
