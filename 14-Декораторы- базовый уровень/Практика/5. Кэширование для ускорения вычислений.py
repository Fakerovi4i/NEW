import functools

def Cache(func):
    cash_dict = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in cash_dict:
            res = func(*args, **kwargs)
            cash_dict[cache_key] = res
        return cash_dict[cache_key]
    return wrapper




@Cache
def fibonachi(num):
    if num <= 1:
        return num
    return fibonachi(num-1) + fibonachi(num - 2)

print(fibonachi(10))
print(fibonachi(15))
print(fibonachi(10))




