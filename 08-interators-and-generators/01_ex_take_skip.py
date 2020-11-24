class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0
        self.counter = 1

    def __iter__(self):
        self.current = 0
        self.counter = 1
        return self

    def __next__(self):
        value = self.current
        self.current += self.step
        if self.counter == self.count + 1:
            raise StopIteration
        self.counter += 1
        return value


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
