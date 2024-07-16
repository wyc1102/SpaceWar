import pygame


class Setting:
    def __init__(self):
        self.init_setting()

    def init_setting(self):
        self.screen_width = 500
        self.screen_height = 800
        self.screen_size = (self.screen_width, self.screen_height)
        self.bg_color = (255, 255, 255)

        self.ship_speed = 2.0
        self.ship_width = 30
        self.ship_height = 30
        self.ship_size = (self.ship_width, self.ship_height)
        self.ship_life_max = 3

        self.buttle_speed = 5.0
        self.buttle_color = (0, 0, 0)
        self.buttle_width = 3
        self.buttle_height = 10
        self.buttle_max_number = 10

        self.enemy_down_speed = 1.0
        self.enemy_row_speed = 1.5
        self.enemy_size = (30, 30)
        self.enemy_change_direction_probability = 0.995
        # 这个数代表敌人更改水平移动方向的频率，该数字应该在0~1之间
        # 这个数字越大代表敌人改变水平移动方向的频率越小

        self.enemy_create_probability = 2
        # 这个数代表相同时间内敌人出现的数量，数字越小，敌人越多

        self.enemy_score_add = 10.0

        self.button_bg_color = (0, 255, 0)
        self.button_text_color = (0, 0, 0)
        self.button_width = 200
        self.button_height = 50
        self.button_text_font = pygame.font.SysFont(None, 48)

        self.score_board_text_font = pygame.font.SysFont(None, 30)
        self.score_board_text_color = (30, 30, 30)
