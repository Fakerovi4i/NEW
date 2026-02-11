import math
def cylinder(radius, hight):
	side = 2 * math.pi * radius * hight
	full = side + 2 * (math.pi * radius ** 2) # (math.pi * radius ** 2) - Это площадь круга S
	return side, full

radius_1 = float(input("Радиус: "))
hight_1 = float(input("Введите высоту: "))

side, full = cylinder(radius_1, hight_1)
print("Площадь боковой поверхности:", round(side, 2))
print("Площадь боковой поверхности:", round(full, 2))