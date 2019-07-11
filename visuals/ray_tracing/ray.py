import math
import pygame

WHITE = (255, 255, 255)


class Vector:
    """represents a 2d vector with a start, end point, magnitude and direction"""

    def __init__(self, x, y, angle, magnitude=500, color=WHITE, width=1):
        self.offset_x = x
        self.offset_y = y
        self.angle = angle
        self.magnitude = magnitude
        self.color = color
        self.width = width

    def get_start(self):
        return (self.offset_x, self.offset_y)

    def get_end(self):
        return (
            self.offset_x + self.magnitude * math.cos(self.angle),
            self.offset_y + self.magnitude * math.sin(self.angle)
        )

    def draw(self, screen):
        pygame.draw.line(
            screen,
            self.color,
            self.get_start(),
            self.get_end(),
            self.width
        )

    def update_magnitude(self, ray):
        """
        updates the ray magnitude such that the currect ray(self)
        stops at the intersection of the provided ray
        returns the point of intersection (None if there is no intersection)
        reference: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
        """
        x_1, y_1 = self.get_start()
        x_2, y_2 = self.get_end()

        x_3, y_3 = ray.get_start()
        x_4, y_4 = ray.get_end()

        den = (x_4 - x_3) * (y_1 - y_2) - (x_1 - x_2) * (y_4 - y_3)

        if den == 0:
            return None

        num1 = (y_3 - y_4) * (x_1 - x_3) + (x_4 - x_3) * (y_1 - y_3)
        num2 = (y_1 - y_2) * (x_1 - x_3) + (x_2 - x_1) * (y_1 - y_3)

        t = num1 / den
        u = num2 / den

        if 0 <= t <= 1 and 0 <= u <= 1:
            intersection = [x_1 + t * (x_2 - x_1), y_1 + t * (y_2 - y_1)]
            self.magnitude = min(
                Vector.get_distance(intersection, self.get_start()),
                self.magnitude
            )
            return intersection

        return None

    @staticmethod
    def get_distance(point_1, point_2):
        """standard distance between two points formula"""
        return math.sqrt(
            math.pow(point_2[0] - point_1[0], 2)
            +
            math.pow(point_2[1] - point_1[1], 2)
        )
