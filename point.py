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
