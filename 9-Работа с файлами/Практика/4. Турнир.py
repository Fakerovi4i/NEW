import os
def fast_sort(li_st):
	if len(li_st) < 2:
		return li_st
	else:
		base = li_st[0][2]
		middle = [li_st[i] for i in range(len(li_st)) if li_st[i][2] == base]
		less = [li_st[i] for i in range(len(li_st)) if li_st[i][2] < base]
		grater = [li_st[i] for i in range(len(li_st)) if li_st[i][2] > base]
	return	fast_sort(grater) + middle + fast_sort(less) #Сортировка от большего к меньшему

first_tour_path_open = open(os.path.abspath('first_tour.txt'), 'r')
first_tour_path_read = first_tour_path_open.read().split('\n')
points_level = int(first_tour_path_read[0])
first_tour_path_open.close()

second_tour = open('second_tour.txt', 'w')
new_tour_list = []

for i_num_str in range(1, len(first_tour_path_read)):
	sur_name_point_list = first_tour_path_read[i_num_str].split()
	if int(sur_name_point_list[2]) > points_level:
		new_tour_list.append(sur_name_point_list)

new_tour_list_sort = fast_sort(new_tour_list)
second_tour.write("".join(['Count pretendent: ', str(len(new_tour_list_sort)), '\n']))

for i_str in range(len(new_tour_list_sort)):
	second_tour.write('\n{}) '.format(str(i_str+1), end=""))
	second_tour.write(
		'{}. {} {}'.format(
			new_tour_list_sort[i_str][1][0], new_tour_list_sort[i_str][0], new_tour_list_sort[i_str][2]
		)
	)

second_tour.close()

# def write_to_file(lst_player):
#     sec_tour_open = open("second_tour.txt", "w")
#     sec_tour_open.write(str(len(lst_player))+"\n")
#
#     for i_index, i_data in enumerate(lst_player):
#         to_write_line = f"{i_index+1}) {i_data[1][:1]}. {i_data[2]} {i_data[0]}\n"
#         sec_tour_open.write(to_write_line)
#     sec_tour_open.close()
#
#
# def team_win(file_name):
#     file = open(file_name, "r")
#     all_file = file.read()
#     file.close()
#
#     all_lines_pretends = all_file.split("\n")
#     points_to_win = int(all_lines_pretends[0])
#
#     player_list = []
#
#     for i in range(1, len(all_lines_pretends)):
#         line = all_lines_pretends[i]
#         if line:
#             i_player_list = line.split()
#
#             if len(i_player_list) == 3:
#                 surname = i_player_list[0]
#                 name = i_player_list[1]
#                 points = int(i_player_list[2])
#
#                 if points > points_to_win:
#                     player_list.append([points, surname, name])
#
#     player_list.sort()
#     player_list.reverse()
#
#     write_to_file(player_list)
#
#
# team_win("first_tour.txt")



