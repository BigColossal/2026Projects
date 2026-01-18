import pygame as pg
from paddles import Paddle
from points import PointSystem
from constants import SCREEN_WIDTH

class Renderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pg.font.SysFont('Arial', 32)

        self.initialize()

    def initialize(self):
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Flame Pong")

    def fill_screen(self, rgb: tuple[int, int, int]):
        self.screen.fill(rgb)

    def fill_paddle(self, paddle: Paddle):
        paddle_x, paddle_y = paddle.pos
        paddle_rect = (paddle_x, paddle_y, paddle.width, paddle.height)
        self.screen.fill(paddle.color, paddle_rect)

    def fill_ball(self, ball):
        pg.draw.circle(self.screen, ball.color, ball.pos, ball.radius)

    def fill_points(self):
        self.screen.blit(self.player_points_txt, (150, 25))
        self.screen.blit(self.enemy_points_txt, (SCREEN_WIDTH - 150, 25))

    def update_points_text(self, pointSystem: PointSystem):
        self.player_points_txt = self.font.render(str(pointSystem.player_points), True, (255, 255, 255))
        self.enemy_points_txt = self.font.render(str(pointSystem.enemy_points), True, (255, 255, 255))