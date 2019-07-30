import pygame
import math
from pygame.locals import *

WHITE = (255, 255, 255)
GREEN = (100, 255, 100)


def draw_tree(screen, start_pos=(250, 500), length=100, angle=-90, level=10, spread=20, scale=0.8):
    if level == 0:
        return

    rad = angle * math.pi / 180

    end_pos = (length * math.cos(rad) +
               start_pos[0], length * math.sin(rad) + start_pos[1])

    pygame.draw.line(
        screen,
        GREEN,
        start_pos,
        end_pos,
        level
    )

    draw_tree(screen, end_pos, length * scale,
              angle - spread, level - 1, spread, scale)
    draw_tree(screen, end_pos, length * scale,
              angle + spread, level - 1, spread, scale)


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    clock = pygame.time.Clock()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)

    level = 0

    # Event loop
    while 1:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))

        draw_tree(
            screen,
            start_pos=(500, 1000),
            length=500,
            angle=-90,
            level=level,
            spread=level * 10,
            scale=0.6
        )
        if level < 10:
            level += 1

        pygame.display.flip()


if __name__ == '__main__':
    main()
