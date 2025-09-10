n = 5   # must be odd
for i in range(0, n, 2):
    print(" " * (i // 2) + "*" * (n - i))
# Bottom half
for i in range(n - 3, -1, -2):
    print(" " * (i // 2) + "*" * (n - i))