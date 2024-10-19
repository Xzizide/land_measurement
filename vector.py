import geometry
import point


class Vector:
    def __init__(self, initial_point: point.Point, terminal_point: point.Point):
        self.initial_point = initial_point
        self.terminal_point = terminal_point

        direction = []
        initial_coords, terminal_coords = self.initial_point.equal_amount_coords(
            self.terminal_point
        )
        for index, coordinate in enumerate(initial_coords):
            direction.append(terminal_coords[index] - coordinate)

        self.direction = point.Point(direction)

    def magnitude(self) -> float:
        return self.initial_point.distance_from(self.terminal_point)

    def __add__(self, other) -> "Vector":
        return self.direction + other.direction
