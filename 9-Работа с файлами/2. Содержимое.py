import os

dir_name = "School"
abs_path_dir = os.path.abspath(os.path.join("..", "..", dir_name))
print(f"Содежимое дерриктории {abs_path_dir}:")

for i_file in os.listdir(abs_path_dir):
    path_to_file = os.path.join(abs_path_dir, i_file)
    print("  ", path_to_file)
