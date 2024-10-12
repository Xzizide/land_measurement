import point

point_1 = point.Point(5)

point_2 = point.Point(2, 5, more_dimensions=[0, 0, 0, 5])

print(point_1.distance_from(point_2))
