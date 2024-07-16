class ScoreBoard:
    def __init__(self, main_game):
        self.main_game = main_game
        self.screen = self.main_game.screen
        self.screen_rect = self.main_game.screen_rect
        self.setting = self.main_game.setting
        self.text_font = self.setting.score_board_text_font
        self.text_color = self.setting.score_board_text_color
        self.score = self.main_game.score
        self.init_board()

    def init_board(self):
        self.init_score()
        self.init_life()

    def init_score(self):
        rounded_score = int(round(self.score, -1))
        score_str = "score:" + "{:,}".format(rounded_score)
        self.score_image = self.text_font.render(
            score_str, True, self.text_color, self.setting.bg_color
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def init_life(self):
        life_str = "life:" + str(self.main_game.life)
        self.life_image = self.text_font.render(
            life_str, True, self.text_color, self.setting.bg_color
        )
        self.life_rect = self.life_image.get_rect()
        self.life_rect.right = self.screen_rect.right - 20
        self.life_rect.top = self.score_rect.bottom + 10

    def draw_score_board(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.life_image, self.life_rect)
