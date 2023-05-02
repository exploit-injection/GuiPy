class Point:
    # Create a class constructor
    def __init__(self, x, y):
        # Properties object
        self.x = x  # create field x
        self.y = y  # create field y

    def distance_to(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5