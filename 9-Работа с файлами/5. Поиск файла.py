import os

def find_dir(abs_dir, file_name, list_path=None):
    # print("Переходим в:", abs_path)
    if list_path == None:
        list_path = []

    for i_elem in os.listdir(abs_dir):
        path = os.path.join(abs_dir, i_elem)
        # print("    Смотрим:", path)

        if i_elem == file_name:
            list_path.append(path)

        if os.path.isdir(path):
            # print("Это дриектория!")
            find_dir(path, file_name, list_path)

    return list_path


abs_path = os.path.abspath("School")
file_name = "test_2.txt"
# print(abs_path)

list_pths = find_dir(abs_path, file_name)

if list_pths:
    print("найденны пути:")
    for i in list_pths:
        print(i)
else:
    print("Ниче нет")
