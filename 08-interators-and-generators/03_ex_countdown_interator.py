class countdown_iterator:

    def __init__(self, count):
        self.count = count
        self.__current = count

    def __iter__(self):
        self.__current = self.count
        return self

    def __next__(self):
        value = self.__current
        if value == -1:
            raise StopIteration
        self.__current -= 1
        return value


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
