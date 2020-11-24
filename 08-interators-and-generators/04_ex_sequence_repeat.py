class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        self.index = 0

        return self

    def __next__(self):
        index = self.index
        if index == self.number:
            raise StopIteration
        self.index += 1
        return self.sequence[index % len(self.sequence)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
