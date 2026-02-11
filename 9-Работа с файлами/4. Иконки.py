import os

file_name = "Dogs.py"
path = os.path.join("School", "2-Базовые коллекции 1 - list (списки)", "Практика 1", file_name)

file_path = os.path.abspath(path)

if os.path.isfile(file_path):
    print("Это файл.")
    print(f"Размер: {os.path.getsize(file_path)}")
elif os.path.isdir(file_path):
    print("Это директория.")
elif os.path.islink(file_path):
    print("Это ссылка.")
elif not os.path.exists(file_path):
    print("Указанного пути не cуществует.")


print(file_path)
