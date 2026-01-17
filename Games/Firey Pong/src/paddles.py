from constants import SCREEN_HEIGHT, SCREEN_WIDTH, EASY_AI_SPEED
import pygame as pg

class Paddle:
    def __init__(self, player=False):
        self.player = player
        self.width = 15
        self.height = 80
        self.color = (255, 255, 255)
        self.pos = pg.Vector2(0, 0)

        self.initialize_positions()

    def initialize_positions(self):
        if self.player == True:
            x_pos = 50
        else:
            x_pos = SCREEN_WIDTH - 50 - self.width

        y_pos = (SCREEN_HEIGHT / 2) - (self.height / 2)
        self.pos = pg.Vector2(x_pos, y_pos)

    def move(self, amount):
        self.pos.y += amount

    def ai_move(self, ball):
        if ball.pos.y <= self.pos.y + (self.height / 2) - 5:
            self.pos.y -= EASY_AI_SPEED
        elif ball.pos.y >= self.pos.y + (self.height / 2) + 5:
            self.pos.y += EASY_AI_SPEED