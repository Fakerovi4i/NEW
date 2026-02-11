class Point():
    __counter = 0

    def __init__(self, x=0, y=0):
        self.set_x(x)
        self.set_y(y)
        Point.__counter += 1

    def __str__(self):
        return (f"Координата X: {self.__x}\n"
                f"Координата Y: {self.__y}\n"
                f"Количество точек: {self.__counter}\n")

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if isinstance(x, (int, float)):
            self.__x = x
        else:
            raise ValueError("Введенные данные не являются числом")

    def get_y(self):
        return self.__y

    def set_y(self, y):
        if isinstance(y, (int, float)):
            self.__y = y
        else:
            raise Exception("Введенные данные не являются числом")

point_1 = Point()
print(point_1)

point_2 = Point()
point_2.set_x(50)
point_2.set_x(20.5)
print(point_2)
