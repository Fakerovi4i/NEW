import os

def error_log_generator(path):
    with open(path, "r", encoding="utf-8") as log_file:
        for line in log_file:
            if "ERROR" in line:
                yield line


path = os.path.abspath("warandpeace.txt")

with open("error.log", "w", encoding="utf-8") as f:
    generator_logs = error_log_generator(path)
    for i_log in generator_logs:
        f.write(i_log)