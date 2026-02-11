class Point():
    counter = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.counter += 1

    def point_info(self):
        print(
            f"Координата X: {self.x}\n"
            f"Координата Y: {self.y}\n"
            f"Количество точек: {self.counter}\n")


point_1 = Point()
point_1.point_info()

point_2 = Point(20, 10)
point_2.point_info()