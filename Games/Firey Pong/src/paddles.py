from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Paddle:
    def __init__(self, player=False):
        self.player = player
        self.width = 15
        self.height = 80
        self.color = (255, 255, 255)
        self.pos = (0, 0)

        self.initialize_positions()

    def initialize_positions(self):
        if self.player == True:
            x_pos = 50
        else:
            x_pos = SCREEN_WIDTH - 50 - self.width

        y_pos = (SCREEN_HEIGHT / 2) - (self.height / 2)
        self.pos = (x_pos, y_pos)

    def move(self, amount):
        past_x, past_y = self.pos
        self.pos = (past_x, past_y + amount)