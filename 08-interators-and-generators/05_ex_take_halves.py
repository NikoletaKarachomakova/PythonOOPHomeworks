def integers():
    i = 1
    while True:
        yield i
        i += 1


def halves():
    for x in integers():
        yield x / 2


def take(n, seq):
    result = []
    for _ in range(n):
        result.append(next(seq))
    return result

def solution():
    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
