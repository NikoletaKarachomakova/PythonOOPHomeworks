class custom_range:

    def __init__(self, start, end):
        self.index = start
        self.end = end

    def __iter__(self):
        return self
    # defining that the self object is iterable. We are making it iterable
    # we will not return self if we move the __next__ into another class
    # then it will return the info requested from the other class

    def __next__(self):
        if self.index <= self.end:
            index = self.index
            self.index += 1
            return index
        raise StopIteration()


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
