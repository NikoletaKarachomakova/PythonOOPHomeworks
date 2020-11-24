class reverse_iter:

    def __init__(self, numbers: list):
        self.numbers = numbers
        self.index = 1

    def __iter__(self):
        self.index = 1
        return self

    def __next__(self):
        current_index = len(self.numbers) - self.index
        if current_index == -1:
            raise StopIteration
        number = self.numbers[current_index]
        self.index += 1
        return number


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
