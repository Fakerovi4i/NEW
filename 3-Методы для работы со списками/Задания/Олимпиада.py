new_team = []
num = 1
people_in_team = 4

while True:
    people_q = int(input('Введите количество участников: '))
    if people_q % people_in_team != 0:
        print("Количество участников должно быть четно", people_in_team)
    else:
        break

for _ in range(people_q//people_in_team):
    new_team.append(list(range(num, num+people_in_team)))
    num += people_in_team

print('Команды:', new_team)