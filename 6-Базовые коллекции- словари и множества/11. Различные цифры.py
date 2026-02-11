text = "ab1n32kz2"

text_set = {i for i in text if "0" <= i <= "9"}

print("Различные цифры строки:", "".join(text_set))