def print_rhombus(n):
    for i in range(1, n+1):
        row = " " * (n-i) + "* " * i
        print(row.rstrip())
    for i in range(n - 1, -1, -1):
        row = " " * (n-i) + "* " * i
        print(row.rstrip())


print_rhombus(int(input()))

