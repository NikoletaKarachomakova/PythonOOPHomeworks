def multiply(n):  # it receives an argument n and returns the decorator
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs) * n
        return wrapper
    return decorator  #first stop: this is the result of calling multiply(n)



@multiply(3) # "@" is decorating the function. So the "@" should get the info from the decorator
#it needs to enter the decorator, to go through wrapper and receive the info from it
def add_ten(number):
    return number + 10

print(add_ten(3))
