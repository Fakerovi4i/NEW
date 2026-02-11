def my_for(iter_obj):
    iterator = iter(iter_obj)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

lst = [1, 2, 3, 4]

my_for(lst)