from typing import Callable, Any

def func_1(num: int) -> int:
    return num + 10

def func_2(func: Callable, *args, **kwargs) -> Any:
    result_func = func(*args, **kwargs)
    return result_func**2

my_func = func_2(func_1, 9)
print(my_func)