import point as pt


# print(point1.x, point1.y)
# print(point2.x, point2.y)
#
# print(point1.distance_to(point2))
# print(point2.distance_to(point1))
# print(point1.distance_to(point1))
# print(point2.distance_to(point2))
#
# print(point1)
# print(point2)

point3D_1 = pt.Point3D(2, 4, 9)
point3D_2 = pt.Point3D(5, 14, -29)

print(point3D_1.z)
print(point3D_1.distance_to(point3D_2))
print(point3D_1.distance3d_to(point3D_2))

print(point3D_1)
print(point3D_1.hello())

point1 = pt.Point(2, 4)
point2 = pt.Point(5, 14)

print(point1.hello())
