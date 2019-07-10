import random
import pygame


def random_color():
    levels = range(32, 256, 32)
    return tuple(random.choice(levels) for _ in range(3))


class ArrayRenderItem:
    """ class to render a rectangle proportional to a value """

    def __init__(self, value, x, y, width):
        self.value = value
        self.rect = pygame.Rect((x, y), (width, value * 10))
        self.color = random_color()

    def draw(self, canvas, show_value=True):
        """ draw rectangle and the value inside it """
        pygame.draw.rect(canvas, self.color, self.rect)
        if show_value:
            font = pygame.font.Font(None, 15)
            text = font.render(str(self.value), 1, (255, 255, 255))
            canvas.blit(
                text, (self.rect.center[0] - 5, self.rect.center[1] - 5))

    def move(self, x_offset, y_offset):
        """ translate the rectangle by an offset """
        self.rect = pygame.Rect(
            (self.rect.x + x_offset, self.rect.y + y_offset), (self.rect.width, self.rect.height))

    def swap(self, item):
        """ swaps values with another item """
        self.value, item.value = item.value, self.value
        self.color, item.color = item.color, self.color
        self.rect.height = self.value * 10
        item.rect.height = item.value * 10


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1000, 400))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock = pygame.time.Clock()

    value_array = []
    for _ in range(40):
        value_array.append(random.randint(1, 35))
    square_array = gen_squares(value_array, side=20)

    current_index = 0

    # Event loop
    while 1:
        # 10 fps
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(background, (0, 0))

        if current_index == len(square_array) - 1:
            current_index = 0

        if square_array[current_index].value > square_array[current_index+1].value:
            square_array[current_index].swap(square_array[current_index + 1])
        for square in square_array:
            square.draw(screen)
        pygame.display.flip()
        current_index += 1


def gen_squares(value_array, side=20, start_x=10, start_y=10):
    square_array = []

    for index, val in enumerate(value_array):
        square_array.append(
            ArrayRenderItem(value=val, x=start_x + index*side, y=start_y, width=side))
    return square_array


if __name__ == '__main__':
    main()
