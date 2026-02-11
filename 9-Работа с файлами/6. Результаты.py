import os
os.chdir("C:\\")
path = os.path.abspath(os.path.join("task", "group_1.txt"))
path_2 = os.path.abspath(os.path.join("task", "Additional_info", "group_2.txt"))

file = open(path, 'r', encoding="utf-8")

summa = 0
diff = 0
for i_line in file:
    info = i_line.split()
    summa += int(info[2])
    diff -= int(info[2])
    print(info)
file.close()

file_2 = open(path_2, "r", encoding="utf-8")

compose = 1
for i_line in file_2:
    info = i_line.split()
    compose *= int(info[2])
    print(info)
file_2.close()

print(summa)
print(diff)
print(compose)
