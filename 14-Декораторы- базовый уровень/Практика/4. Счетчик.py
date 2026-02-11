def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Вызываем функцию {wrapper.count}-й раз.")
        result = func(*args, **kwargs)
        return result
    wrapper.count = 0
    return wrapper


@counter
def test():
    print('Привет!!')


@counter
def test_2():
    print("Пока!")


test()
test()
test_2()