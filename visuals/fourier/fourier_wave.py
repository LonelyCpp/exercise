"""
https://en.wikipedia.org/wiki/Fourier_series#Convergence
"""
import pygame
from pygame.locals import *
import math
import copy

BLACK = (0, 0, 0)


class SquareWave():
    def get_radius(self, circle_index, base_radius):
        n = circle_index * 2 + 1
        return base_radius * (4 / (n * math.pi))

    def get_position(self, circle_index, time):
        n = circle_index * 2 + 1
        return [math.cos(n * time), math.sin(n * time)]


class SawtoothWave():
    def get_radius(self, circle_index, base_radius):
        n = circle_index + 1
        return base_radius * (2 / (n * math.pi))

    def get_position(self, circle_index, time):
        n = circle_index + 1
        return [math.cos(n * time), math.sin(n * time)]


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1500, 500))
    pygame.display.set_caption('square wave')
    clock = pygame.time.Clock()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    center_pos = [300, background.get_rect().centery]
    time = 0
    BASE_RADIUS = 80
    ITERATIONS = 5

    wave_positions = []

    # Event loop
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))

        line_end_x = 0
        line_end_y = 0
        circle_center = copy.deepcopy(center_pos)

        # wave = SquareWave()
        wave = SawtoothWave()

        for circle_index in range(ITERATIONS):
            radius = abs(wave.get_radius(circle_index, BASE_RADIUS))

            # circle
            pygame.draw.circle(screen, BLACK, circle_center, int(radius), 1)

            line_end_x, line_end_y = wave.get_position(circle_index, time)

            # scale offset
            line_end_x *= radius
            line_end_y *= radius

            # translate offset
            line_end_x += circle_center[0]
            line_end_y += circle_center[1]

            # radius line
            pygame.draw.line(screen, BLACK, circle_center,
                             [line_end_x, line_end_y], 1)

            circle_center = [int(line_end_x), int(line_end_y)]

        pygame.draw.line(screen, BLACK,
                         [line_end_x, line_end_y], [500, line_end_y], 1)

        for i in range(len(wave_positions)):
            wave_positions[i][0] += 1

        wave_positions.insert(0, [500, line_end_y])

        if len(wave_positions) > 2:
            pygame.draw.lines(screen, BLACK, False, wave_positions)

        if len(wave_positions) > 1000:
            wave_positions.pop()

        pygame.display.flip()
        time += 0.05


if __name__ == '__main__':
    main()
