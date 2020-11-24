class vowels:
    def __init__(self, text: str):
        self.text = text
        self.idx = 0

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        while self.idx < len(self.text):
            current_ch = self.text[self.idx]
            self.idx += 1
            if current_ch.lower() in ('a', 'e', 'i', 'o', 'u'):
                return current_ch
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)


