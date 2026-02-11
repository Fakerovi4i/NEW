def my_gen(file_name):
    with open(file_name, "r") as file:
        for line in file:
            num_str = ""
            for char in line:
                if not char.isspace():
                    num_str += char
                elif num_str:
                    yield int(num_str)
                    num_str = ''
            if num_str:
                yield int(num_str)


total = sum(my_gen("numbers.txt"))
print(total)


