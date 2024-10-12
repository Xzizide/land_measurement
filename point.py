class Point:
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        z: float = 0,
        w: float = 0,
        more_dimensions: list[float] = None,
    ):
        self.coordinates = {"x": x, "y": y, "z": z, "w": w}
        if more_dimensions:
            index = 5
            for coordinate in more_dimensions:
                self.coordinates[str(index)] = coordinate
                index += 1

    def distance_from(self, obj: "Point") -> float:
        distance = 0

        if len(self.coordinates) > len(obj.coordinates):
            more_valued_dimensions = self.coordinates
        else:
            more_valued_dimensions = obj.coordinates

        for coordinate in more_valued_dimensions:
            temp_self_coord = 0
            temp_obj_coord = 0
            if coordinate in self.coordinates:
                temp_self_coord = self.coordinates[coordinate]
            if coordinate in obj.coordinates:
                temp_obj_coord = obj.coordinates[coordinate]

            distance += (temp_obj_coord - temp_self_coord) ** 2

        return distance ** (1 / 2)
