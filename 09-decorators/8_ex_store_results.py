class store_results:
    def __init__(self, function):
        self.func = function

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a") as f:
            self.result = self.func(*args, **kwargs)
            f.write(f"Function '{self.func.__name__}' was called. Result: {self.result}\n")


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b


with open("results.txt", "w") as f:
    pass

add(2, 2)
mult(6, 4)
