import geometry


class Point:
    def __init__(self, dimensions: list[float] = None):
        self.coordinates = []

        if dimensions:
            for coordinate in dimensions:
                self.coordinates.append(coordinate)
        else:
            self.coordinates.append(0)

    def distance_from(self, other: "Point") -> float:
        distance = 0

        self_coords, other_coords = geometry.equal_amount_list(
            list_1=self.coordinates, list_2=other.coordinates
        )

        for index, coordinate in enumerate(self_coords):
            distance += (other_coords[index] - coordinate) ** 2

        return distance ** (1 / 2)

    def __str__(self) -> str:
        coords_string = "("
        for coordinate in self.coordinates:
            coords_string += str(coordinate) + ","
        coords_string = coords_string[:-1] + ")"
        return coords_string

    def __add__(self, other) -> "Point":
        self_coords, other_coords = geometry.equal_amount_list(
            list_1=self.coordinates, list_2=other.coordinates
        )
        added_coords = []

        for index, coordinate in enumerate(self_coords):
            added_coords.append(coordinate + other_coords[index])

        return Point(dimensions=added_coords[:])

    def __sub__(self, other) -> "Point":
        return self + (other * -1)

    def __mul__(self, other) -> "Point":
        if type(other) is Point:
            total = 0
            self_coords, other_coords = geometry.equal_amount_list(
                list_1=self.coordinates, list_2=other.coordinates
            )
            for index, coord in enumerate(self_coords):
                total += coord + other_coords[index]
            return total

        multiplied_coords = []

        for coord in self.coordinates:
            multiplied_coords.append(coord * other)

        return Point(dimensions=multiplied_coords[:])

    def __truediv__(self, other) -> "Point":
        if type(other) is Point or other == 0:
            raise

        divided_coords = []

        for coord in self.coordinates:
            divided_coords.append(coord / other)

        return Point(dimensions=divided_coords[:])
