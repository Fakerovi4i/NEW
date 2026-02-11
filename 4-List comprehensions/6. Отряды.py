import random
team_1 = [random.randint(50, 80) for _ in range(10)]
team_2 = [random.randint(30, 60) for _ in range(10)]
team_3 = ['Погиб' if team_1[i_damage] + team_2[i_damage] >= 100
		  else 'Выжил'
		  for i_damage in range(10)]

print(team_1)
print(team_2)
print(team_3)