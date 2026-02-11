# N = int(input("Количество сотрудников: "))
# salary_list = []
#
# for emp in range(N):
# 	print(f"Введите зарплату {emp+1} сотрудника:", end = " ")
# 	sal = int(input())
# 	salary_list.append(sal)
# for i in salary_list:
# 	if i == 0:
# 		salary_list.remove(0)
#
# print("Осталось сотрудников:", len(salary_list))
# print("Зарплаты:", salary_list)
# print("Максимальная зарплата:", max(salary_list))
# print("Минимальная зарплата:", min(salary_list))

#Второй вариант мне кажется лучше

people_count = 6
sellery = []

for i_people in range(people_count):
    print(f"Зарплата {i_people + 1} сотрудника:", end=' ')
    one_sellery = int(input())
    sellery.append(one_sellery)

for i in range(sellery.count(0)):
    sellery.remove(0)

print("Осталось сотрудников:", len(sellery))
print('Зарплаты:', sellery)
print('Минимальная зарплата:', min(sellery))
print("Максимальная зарплата:", max(sellery))