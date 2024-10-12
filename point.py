class Point:
    def __init__(self, dimensions: list[float] = None):
        self.coordinates = []

        if dimensions:
            for coordinate in dimensions:
                self.coordinates.append(coordinate)

        dimension_diff = 4 - len(self.coordinates)

        if dimension_diff > 0:
            for index in range(dimension_diff):
                self.coordinates.append(0)

        self.x = self.coordinates[0]
        self.y = self.coordinates[1]
        self.z = self.coordinates[2]
        self.w = self.coordinates[3]

    def equal_amount_coords(self, other: "Point") -> tuple[list[float], list[float]]:
        self_coords_copy = self.coordinates[:]
        other_coords_copy = other.coordinates[:]
        difference = len(self_coords_copy) - len(other_coords_copy)

        if difference > 0:
            for index in range(difference):
                other_coords_copy.append(0)
        else:
            for index in range(abs(difference)):
                self_coords_copy.append(0)

        return self_coords_copy, other_coords_copy

    def distance_from(self, other: "Point") -> float:
        distance = 0

        self_coords, other_coords = self.equal_amount_coords(other)

        for index, coordinate in enumerate(self_coords):
            distance += (other_coords[index] - coordinate) ** 2

        return distance ** (1 / 2)

    def __add__(self, other) -> "Point":
        self_coords, other_coords = self.equal_amount_coords(other)
        added_coords = []

        for index, coordinate in enumerate(self_coords):
            added_coords.append(coordinate + other_coords[index])

        return Point(dimensions=added_coords[:])
