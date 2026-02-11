players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

team_a_rest = [
	i_player["name"] for i_player in players_dict.values()
	if i_player["team"] == "A" and i_player["status"] == "Rest"
]

team_b_trein = [
	i_player["name"] for i_player in players_dict.values()
	if i_player["team"] == "B" and i_player["status"] == "Training"
]

team_c_travel = [
	i_player["name"] for i_player in players_dict.values()
	if i_player["team"] == "C" and i_player["status"] == "Travel"
]

print("Команда A:", team_a_rest)
print("Команда B:", team_b_trein)
print("Команда C:", team_c_travel)
