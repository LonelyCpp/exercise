import math
from ray import Vector
import random
import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('square wave')
    clock = pygame.time.Clock()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    walls = []
    for _ in range(20):
        walls.append(
            Vector(
                random.randint(50, 950),
                random.randint(50, 950),
                angle=random.randint(0, 6),
                magnitude=random.randint(100, 500),
                color=RED,
                width=3
            ))

    # Event loop
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        rays = []
        angle = 0

        for wall in walls:
            wall.draw(screen)

        while angle < math.pi * 2:
            ray = Vector(mouse_pos[0], mouse_pos[1], angle, color=GREEN)
            rays.append(ray)
            for wall in walls:
                ray.update_magnitude(wall)

            angle += 0.025

        for ray in rays:
            ray.draw(screen)

        pygame.display.flip()


if __name__ == '__main__':
    main()
