import os
import random

def find_dir(abs_dir, file_name, list_path=None):
    if list_path == None:
        list_path = []

    for i_elem in os.listdir(abs_dir):
        path = os.path.join(abs_dir, i_elem)

        if i_elem == file_name:
            list_path.append(path)

        if os.path.isdir(path):
            find_dir(path, file_name, list_path)

    return list_path

abs_path = os.path.abspath("School")
file_name = "test_2.txt"

list_pths = find_dir(abs_path, file_name)

if list_pths:
    print("Найденны пути:")
    opn_file = open((list_pths[random.randint(0, len(list_pths) - 1)]), "r", encoding="utf-8")
    print(opn_file.read())
    opn_file.close()
else:
    print("Ниче нет")








