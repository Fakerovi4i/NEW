def isPalindrome(string):
    text_dict = dict()
    for i in string:
        text_dict[i] = text_dict.get(i, 0) + 1

    odd_count = 0
    for i in text_dict.values():
        if i % 2 != 0:
            odd_count += 1
        if odd_count > 1: #Если нечетных больше 1, то сделать палиндром нельзя
            return False
    return  True

log_count = 0
counter_pall = 0
open_file = open("words.txt", "r", encoding="utf-8")
open_log_file = open("log_pal.log", 'a', encoding="utf-8")

for i_line in open_file:
    i_line = i_line.strip()
    try:
        if not i_line.isalpha():
            raise ValueError
        if isPalindrome(i_line):
            counter_pall += 1
    except ValueError:
        log_count += 1
        print(f"Встречена {log_count}-ая ошибка;")
        open_log_file.write(f"['{i_line}' - строка содержит цифры;]\n")

open_log_file.close()
open_file.close()










