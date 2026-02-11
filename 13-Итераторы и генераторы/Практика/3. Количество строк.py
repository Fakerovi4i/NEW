import os

def gen_sum_dir(path):
    for i_file in os.listdir(path):
        file_path = os.path.join(path, i_file)

        if not (i_file.endswith(".py") and os.path.isfile(file_path)):
            continue

        counter = 0
        with open(file_path, "r", encoding="utf-8") as file:
            for i_str in file:
                i_str = i_str.strip()
                if not i_str:
                    continue

                if "#" in i_str:
                    i_str = i_str.split("#")[0].strip()
                    if not i_str:
                        continue
                counter += 1
        yield counter

path = r"D:\My_python\My_projects\School\13-Итераторы и генераторы\Практика"
print(sum(gen_sum_dir(path)))