
words_list = input("Введите три слова, через пробел: ").split()
text = input("Введите текст: ").split()

count_list = [[words_list[i], text.count(words_list[i])] for i in range(len(words_list))]


print(count_list)



