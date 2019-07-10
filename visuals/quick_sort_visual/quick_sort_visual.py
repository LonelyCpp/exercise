import random
import threading
import time
import pygame

screen = pygame.display.set_mode((1000, 400))
pygame.display.set_caption('Basic Pygame program')

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))
clock = pygame.time.Clock()


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


def quick_sort_partition(arr, low, high):
    i = low - 1
    pivot = arr[high].value

    for j in range(low, high):
        if arr[j].value <= pivot:
            i = i+1
            arr[i].swap(arr[j])
            pygame.event.post(pygame.event.Event(
                pygame.USEREVENT, event_code='quick_sort_update'))
            time.sleep(0.2)

    arr[i+1].swap(arr[high])
    pygame.event.post(pygame.event.Event(
        pygame.USEREVENT, event_code='quick_sort_update'))

    return (i+1)


def quick_sort(arr, low, high):
    if low < high:
        pivot = quick_sort_partition(arr, low, high)

        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


def main():
    # Initialise screen
    pygame.init()

    # Blit everything to the screen
    # screen.blit(background, (0, 0))
    # pygame.display.flip()

    value_array = []
    for _ in range(40):
        value_array.append(random.randint(1, 35))
    square_array = gen_squares(value_array, side=20)
    redraw(square_array)

    sorting = False

    # # Event loop
    while 1:
        clock.tick(60)
        if not sorting:
            threading.Thread(target=quick_sort, args=(
                square_array, 0, len(square_array)-1)).start()
            # quick_sort(square_array, 0, len(square_array)-1)
            sorting = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.USEREVENT:
                if event.event_code == 'quick_sort_update':
                    redraw(square_array)


def redraw(square_array):
    screen.blit(background, (0, 0))

    for square in square_array:
        square.draw(screen)

    pygame.display.flip()


def gen_squares(value_array, side=20, start_x=10, start_y=10):
    square_array = []

    for index, val in enumerate(value_array):
        square_array.append(
            ArrayRenderItem(value=val, x=start_x + index*side, y=start_y, width=side))
    return square_array


if __name__ == '__main__':
    main()
