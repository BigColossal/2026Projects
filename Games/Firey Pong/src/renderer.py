import pygame as pg
from paddles import Paddle

class Renderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.initialize()

    def initialize(self):
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Firey Pong")

    def fill_screen(self, rgb: tuple[int, int, int]):
        self.screen.fill(rgb)

    def fill_paddle(self, paddle: Paddle):
        paddle_x, paddle_y = paddle.pos
        paddle_rect = (paddle_x, paddle_y, paddle.width, paddle.height)
        self.screen.fill(paddle.color, paddle_rect)