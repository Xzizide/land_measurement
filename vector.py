import point


class Vector:
    def __init__(self, initial_point: point.Point, terminal_point: point.Point):
        self.initial_point = initial_point
        self.terminal_point = terminal_point

    def magnitude(self) -> float:
        return self.initial_point.distance_from(self.terminal_point)
