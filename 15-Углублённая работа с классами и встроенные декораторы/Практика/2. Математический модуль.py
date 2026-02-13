from math import pi

class MyMath:
    """Класс из методов для решения математических вычислений"""
    @staticmethod
    def circle_len(radius: float) -> float:
        """Статический метод расчета длины окуржности"""
        return 2 * pi * radius

    @staticmethod
    def circle_sqr(radius: float)-> float:
        """Статический метод расчета площади круга"""
        return pi * radius**2

    @staticmethod
    def cube_volume(side: float) -> float:
        """Статический метод расчета объема куба"""
        return side**3

    @staticmethod
    def sphere_sqr(radius:float)-> float:
        """Статический метод расчета площади поверхности сферы"""
        return 4 * pi * radius**2

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sqr(radius=6)
res_3 = MyMath.cube_volume(10)
res_4 = MyMath.sphere_sqr(10)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
