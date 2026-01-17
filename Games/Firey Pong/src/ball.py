import pygame as pg
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_INITIAL_SPEED
from random import randint
import math

class Ball:
    def __init__(self):
        self.velocity = pg.Vector2(0, 0)
        self.speed = 0
        self.pos = pg.Vector2(0, 0)
        self.radius = 10
        self.color = (255, 255, 255)

        self.last_hit_by = None

        self.initialize()

    def initialize(self):
        self.pos = pg.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        ball_to_player = randint(1, 2)
        if ball_to_player == 1:
            ball_to_player = True
        else:
            ball_to_player = False

        if ball_to_player:
            self.speed += BALL_INITIAL_SPEED
            self.velocity.x -= BALL_INITIAL_SPEED
        else:
            self.speed += BALL_INITIAL_SPEED
            self.velocity.x += BALL_INITIAL_SPEED
    
    def move(self):
        self.pos += self.velocity

    def check_paddle_collision(self, rect):
        closest_x = max(rect[0], min(self.pos.x, rect[0] + rect[2]))
        closest_y = max(rect[1],  min(self.pos.y, rect[1] + rect[3]))

        dx = self.pos.x - closest_x
        dy = self.pos.y - closest_y

        return dx*dx + dy*dy <= self.radius * self.radius
    
    def check_wall_collision(self):
        if ((self.pos.y - self.radius) <= 0 or (self.pos.y + self.radius) >= SCREEN_HEIGHT) and not self.hit_wall:
            self.velocity.y *= -1
            if (self.pos.y - self.radius) <= 0:
                self.pos.y = 0.1 + self.radius
            else:
                self.pos.y = SCREEN_HEIGHT - 0.1 - self.radius
            self.hit_wall = True
            return
        else:
            self.hit_wall = False
    
    def pong_bounce(self, paddle):
        self.speed += 0.5
        if paddle.player:
            self.last_hit_by = "player"
        else:
            self.last_hit_by = "opponent"
        # 1. distance from paddle center
        offset = self.pos.y - (paddle.pos.y + (paddle.height / 2))

        # 2. normalize (-1 to 1)
        normalized = offset / (paddle.height / 2)

        # optional clamp (prevents insane angles)
        normalized = max(-1, min(1, normalized))

        # 3. max bounce angle (radians)
        max_angle = math.radians(60)

        angle = normalized * max_angle

        # 4. build new velocity
        direction = -1 if self.velocity.x > 0 else 1

        self.velocity.x = math.cos(angle) * self.speed * direction
        self.velocity.y = math.sin(angle) * self.speed