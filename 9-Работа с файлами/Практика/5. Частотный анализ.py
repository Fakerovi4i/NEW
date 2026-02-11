def sort_my(file_list):
    len_list = len(file_list)
    for i in range(len_list):
        for j in range(0, len_list-i-1):
            if file_list[j][0] < file_list[j+1][0]:
                file_list[j], file_list[j+1] = file_list[j+1], file_list[j]
            elif file_list[j][0] == file_list[j+1][0] and file_list[j][1] > file_list[j+1][1]:
                file_list[j+1], file_list[j] = file_list[j], file_list[j+1]

def make_dict(txt_file):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dict_sym = dict()
    for i_sym in txt_file.lower():
        if i_sym in alphabet :
            dict_sym[i_sym] = dict_sym.get(i_sym, 0) + 1
    return dict_sym


def gist_sym(file_name):
    open_file = open(file_name)
    read_file_txt = open_file.read()
    open_file.close()
    dict_file = make_dict(read_file_txt)
    file_list = [(val, key) for key, val in dict_file.items()]
    to_devide = sum(dict_file.values())
    sort_my(file_list)

    open_result = open("analysis.txt", 'w')
    for i in file_list:
        res = round((i[0] / to_devide), 3)
        open_result.write(f"{i[1]} {res}\n")
    open_result.close()


gist_sym("text.txt")
