import point as pt

point1 = pt.Point(1, 33)
point2 = pt.Point(4, -9)


print(point1.x, point1.y)
print(point2.x, point2.y)

print(point1.distance_to(point2))
print(point2.distance_to(point1))
print(point1.distance_to(point1))
print(point2.distance_to(point2))

print(point1)
print(point2)