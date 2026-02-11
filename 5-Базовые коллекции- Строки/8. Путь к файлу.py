path = "C:/user/docs/folder/new_file.txt"
disc_path = input("На каком диске должен быть файл?: ")
path_format = input("Какое расширение?: ")

if not path.startswith(disc_path):
	print("Некоректный диск!")
elif not path.endswith(path_format):
	print("Некоректный формат!")
else:
	print("Путь коректен!")