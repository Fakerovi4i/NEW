import os

def gen_files_path(f_dir, start=None):
    start_dir = os.path.abspath(start)
    for iroot, dirs, files in os.walk(start_dir):
        if os.path.split(iroot)[1] == f_dir:
            for s_root, s_dirs, s_files in os.walk(iroot):
                for file in s_files:
                    yield os.path.join(s_root, file)
                return
    print("Директория не найдена!")


gen_path = gen_files_path("13-Итераторы и генераторы", "/")
for i in gen_path:
    print(i)