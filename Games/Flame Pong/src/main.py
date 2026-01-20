import pygame as pg
from constants import FPS, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_MOVEMENT_SPEED, USER_WIN, USER_LOSS
from renderer import Renderer
from paddles import Paddle
from ball import Ball
from points import PointSystem

pg.init()

def initialize_game():
    player_paddle = Paddle(position="left")
    enemy_paddle = Paddle(position="right")
    ball = Ball()
    points = PointSystem()

    return player_paddle, enemy_paddle, ball, points

def update(paddles: list[Paddle], ball: Ball):
    player1_paddle, player2_paddle = paddles
    check_keyboard_input(player1_paddle)

    for paddle in paddles:
        if ball.last_hit_by == "left":
            if paddle.position == "left":
                continue
            else:
                paddle.ai_move(ball)
        elif ball.last_hit_by == "right" and not paddle.position == "left":
            continue
        
        if ball.check_paddle_collision([paddle.pos[0], paddle.pos[1], paddle.width, paddle.height]):
            ball.pong_bounce(paddle)
    ball.check_wall_collision()
    ball.check_win_condition()
    ball.move()

def render(renderer: Renderer, paddles: list[Paddle], ball: Ball):
    renderer.fill_screen((10, 10, 10))
    for paddle in paddles:
        renderer.fill_paddle(paddle)
    renderer.fill_ball(ball)
    renderer.fill_points()
    pg.display.flip()

def check_keyboard_input(player_paddle):
    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        player_paddle.move(-PLAYER_MOVEMENT_SPEED)

    if keys[pg.K_s]:
        player_paddle.move(PLAYER_MOVEMENT_SPEED)

def main():
    running = True
    clock = pg.time.Clock()
    renderer = Renderer(SCREEN_WIDTH, SCREEN_HEIGHT)
    player_paddle, enemy_paddle, ball, points = initialize_game()
    renderer.update_points_text(points)
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == USER_WIN:
                player_paddle.initialize_positions()
                enemy_paddle.initialize_positions()
                ball.initialize()
                points.increase_player()
                renderer.update_points_text(points)
            elif event.type == USER_LOSS:
                player_paddle.initialize_positions()
                enemy_paddle.initialize_positions()
                ball.initialize()
                points.increase_enemy()
                renderer.update_points_text(points)

        update([player_paddle, enemy_paddle], ball)
        render(renderer, [player_paddle, enemy_paddle], ball)
        clock.tick(FPS)

if __name__ == "__main__":
    main()
