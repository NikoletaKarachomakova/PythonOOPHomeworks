def reverse_text(string):
    idx = len(string)
    while idx > 0:
        idx -= 1
        yield string[idx]


for char in reverse_text("step"):
    print(char, end='')
