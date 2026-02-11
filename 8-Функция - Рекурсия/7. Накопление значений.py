def add_num(num, lst=None):
    if lst == None:
        lst = []
    lst.append(num)
    print(lst)

add_num(5)
add_num(10, lst=[2])
add_num(25)
