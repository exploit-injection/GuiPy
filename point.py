class Point:
    # Create a class constructor
    def __init__(self, x, y):
        # Properties object
        self.x = x  # create field x
        self.y = y  # create field y

    def distance_to(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5

    # Create format output (string)
    def __str__(self):
        str_repr = 'Point({0:.5f}, {1:.5f})'.format(self.x, self.y)
        return str_repr

    def hello(self):
        return 'Hello!!! My coords are: {0:.5f}, {1:.5f}:>)'.format(self.x, self.y)

# Create new Class (use inheritance)
class Point3D(Point):
    def __init__(self, x, y, z):
        Point.__init__(self, x, y)  # init fields (use class Point)
        self.z = z

    def distance3d_to(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2 + (self.z - point.z)**2)**0.5

    def __str__(self):
        str_repr = 'Point({0:.5f}, {1:.5f}, {2:.5f})'.format(self.x, self.y, self.z)
        return str_repr

    def hello(self):
        return 'Hello!!! My coords are: {0:.5f}, {1:.5f}, {2:.5f} :>)'.format(self.x, self.y, self.z)