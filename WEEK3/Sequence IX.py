"""d"""
def generate_pattern():
    """d"""
    size = 2 * n -1
    for i in range(size):
        for j in range(size):
            layer = min(i, j, size - 1 - i, size - 1 - j)
            print(f"{layer + 1:02d}", end=" ")
        print()
n = int(input())
generate_pattern()
