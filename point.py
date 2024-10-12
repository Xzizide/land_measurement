class Point:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0):
        self.coordinates = {"x": x, "y": y, "z": z, "w": w}

    def distance_from(self, obj: "Point"):
        distance = 0

        for coordinate in self.coordinates:
            distance += (
                obj.coordinates[coordinate] - self.coordinates[coordinate]
            ) ** 2

        return distance ** (1 / 2)
