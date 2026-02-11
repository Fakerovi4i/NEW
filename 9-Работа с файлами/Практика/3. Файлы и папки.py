import os

def find_size(path_to_folder):
    summ = 0

    for i_file in os.listdir(path_to_folder):
        item_path = os.path.join(path_to_folder, i_file)
        if os.path.isfile(item_path):
            summ += os.path.getsize(item_path)
        elif if os.path.isdir(item_path):
            summ += find_size(item_path)

    return summ


def find_dir_file(path_to_folder):
    sum_dir = 0
    sum_file = 0

    for i_file in os.listdir(path_to_folder):
        item_path = os.path.join(path_to_folder, i_file)
        if os.path.isfile(item_path):
            sum_file += 1
        elif os.path.isdir(item_path):
            sum_dir += 1
            sub_dir, sub_file = find_dir_file(item_path)
            sum_dir += sub_dir
            sum_file += sub_file
    return sum_dir, sum_file


path = os.path.abspath(os.path.join('School', '5-Базовые коллекции- Строки'))

size = find_size(path) / 1024
q_dir, q_file = find_dir_file(path)

print(f"Размер в килобайтах: {size}\n"
      f"Количество подкатологов: {q_dir}\n"
      f"Количество файлов: {q_file}")