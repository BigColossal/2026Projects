import pygame as pg
from constants import FPS, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_MOVEMENT_SPEED
from renderer import Renderer
from paddles import Paddle

pg.init()

def initalize_game():
    player_paddle = Paddle(player=True)
    enemy_paddle = Paddle()

    return player_paddle, enemy_paddle



def update():
    pass

def render(renderer: Renderer, paddles: list[Paddle]):
    renderer.fill_screen((30, 30, 30))  # dark gray background
    for paddle in paddles:
        renderer.fill_paddle(paddle)
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
    player_paddle, enemy_paddle = initalize_game()
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        check_keyboard_input(player_paddle)

        update()
        render(renderer, [player_paddle, enemy_paddle])
        clock.tick(FPS)


if __name__ == "__main__":
    main()
