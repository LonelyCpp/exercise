class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def compare(point_1, point_2):
        if isinstance(point_1, Point) and isinstance(point_2, Point):
            return point_1.x < point_2.x or (point_1.x == point_2.x and point_1.y < point_2.y)
        raise Exception("expected arguments to be of type 'Point'")

    def clock_wise(self, point_2, point_3):
        if isinstance(point_2, Point) and isinstance(point_3, Point):
            return self.x * (point_2.y - point_3.y) + \
                point_2.x * (point_3.y - self.y) + \
                point_3.x * (self.y - point_2.y) < 0

        raise Exception("expected arguments to be of type 'Point'")

    def counter_clock_wise(self, point_2, point_3):
        if isinstance(point_2, Point) and isinstance(point_3, Point):
            return self.x * (point_2.y - point_3.y) + \
                point_2.x * (point_3.y - self.y) + \
                point_3.x * (self.y - point_2.y) > 0
        raise Exception("expected arguments to be of type 'Point'")

    def get_tuple(self):
        return (self.x, self.y)

    def __iter__(self):
        yield self.x
        yield self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __lt__(self, other):
        if self.x > other.x:
            return False
        if self.x == other.x:
            return self.y < other.y
        return True

    def __gt__(self, other):
        if self.x > other.x:
            return True
        if self.x == other.x:
            return self.y > other.y
        return False

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)
