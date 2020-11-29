def logged(f):
    def wrapper(*args):
        result_func = f(*args)
        result_wrapper = f"you called {f.__name__}{args}\nit returned {result_func}"
        return result_wrapper
    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
