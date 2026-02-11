import os

file_name = "admin.bat"

path_file = os.path.join("access", file_name)
abs_path = os.path.abspath(os.path.join("access", file_name))


print(path_file)
print(abs_path)
