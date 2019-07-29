import pygame
from pygame.locals import *
from point import Point

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)


def convex_hull(point_list):
    """
    Convex Hull construction using Graham's Scan
    https://cp-algorithms.com/geometry/grahams-scan-convex-hull.html
    """
    if len(point_list) <= 1:
        return []

    LIST_LENGTH = len(point_list)

    sorted_list = sorted(point_list)
    lowest_point = sorted_list[0]
    highest_point = sorted_list[LIST_LENGTH - 1]

    up = [lowest_point]
    down = [lowest_point]

    for i in range(LIST_LENGTH):
        if i == LIST_LENGTH - 1 or lowest_point.clock_wise(sorted_list[i], highest_point):
            while len(up) >= 2 and not up[-2].clock_wise(up[-1], sorted_list[i]):
                up.pop()
            up.append(sorted_list[i])
        if i == LIST_LENGTH - 1 or lowest_point.counter_clock_wise(sorted_list[i], highest_point):
            while len(down) >= 2 and not down[-2].counter_clock_wise(down[-1], sorted_list[i]):
                down.pop()
            down.append(sorted_list[i])

    return up + list(reversed(down[:-1]))


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)

    point_list = []
    hull = []

    # Event loop
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                point_list.append(Point(mouse_pos[0], mouse_pos[1]))
                hull = convex_hull(point_list)

        screen.blit(background, (0, 0))

        for point in point_list:
            pygame.draw.circle(
                screen,
                PINK if point in hull else BLUE,
                tuple(point),
                2
            )

        if len(hull) > 2:
            pygame.draw.lines(
                screen,
                RED,
                False,
                list(map(lambda item: tuple(item), hull))
            )

        pygame.display.flip()


if __name__ == '__main__':
    main()
