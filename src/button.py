import pygame


class Button:
    def __init__(self, main_game, message):
        self.main_game = main_game
        self.screen = self.main_game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = self.main_game.setting
        self.message = message
        self.init_button()

    def init_button(self):
        self.width = self.setting.button_width
        self.height = self.setting.button_height
        self.font = self.setting.button_text_font
        self.text_color = self.setting.button_text_color
        self.button_color = self.setting.button_bg_color
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.message_image = self.font.render(
            self.message, True, self.text_color, self.button_color
        )
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self):
        pygame.draw.rect(self.screen, self.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)
