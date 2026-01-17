import pygame as pg
from constants import FPS, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_MOVEMENT_SPEED
from renderer import Renderer
from paddles import Paddle
from ball import Ball

pg.init()

def initalize_game():
    player_paddle = Paddle(player=True)
    enemy_paddle = Paddle()
    ball = Ball()

    return player_paddle, enemy_paddle, ball



def update(paddles: list[Paddle], ball: Ball):
    player_paddle, enemy_paddle = paddles
    check_keyboard_input(player_paddle)

    for paddle in paddles:
        if ball.last_hit_by == "player":
            if paddle.player:
                continue
            else:
                paddle.ai_move(ball)
        elif ball.last_hit_by == "enemy" and not paddle.player:
            continue
        
        if ball.check_paddle_collision([paddle.pos[0], paddle.pos[1], paddle.width, paddle.height]):
            ball.pong_bounce(paddle)
    ball.check_wall_collision()
    ball.move()

def render(renderer: Renderer, paddles: list[Paddle], ball: Ball):
    renderer.fill_screen((30, 30, 30))  # dark gray background
    for paddle in paddles:
        renderer.fill_paddle(paddle)
    renderer.fill_ball(ball)
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
    player_paddle, enemy_paddle, ball = initalize_game()
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        update([player_paddle, enemy_paddle], ball)
        render(renderer, [player_paddle, enemy_paddle], ball)
        clock.tick(FPS)


if __name__ == "__main__":
    main()
