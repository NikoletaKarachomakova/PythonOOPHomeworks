def cache(func):
    log = {}
    def wrapper(n):
        if n not in log:
            result = func(n)
            log[n] = result
            return result

        return log[n]

    wrapper.log = log
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
