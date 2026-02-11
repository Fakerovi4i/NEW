violator_songs = [
['World in My Eyes', 4.86],
['Sweetest Perfection', 4.43],
['Personal Jesus', 4.56],
['Halo', 4.9],
['Waiting for the Night', 6.07],
['Enjoy the Silence', 4.20],
['Policy of Truth', 4.76],
['Blue Dress', 4.29],
['Clean', 5.83]
]

quant_songs = int(input('Сколько песен добавить: '))
duration = 0.0

for i in range(quant_songs):
    song = input(f'Введите название {i+1}-й песни: ')
    for j in violator_songs:
        if song in j:
            duration += j[1]

print('Общая продолжительность:', round(duration, 2))