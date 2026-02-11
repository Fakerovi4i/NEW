violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}
songs_quant = 3
sum_time = 0

for i_song in range(songs_quant):
	print("\nВведите название {0}-ой песни:".format(i_song+1), end=" ")
	song = input()
	sum_time += violator_songs.get(song, 0)

print("Общее время звучания песен:", round(sum_time, 2), "минут")