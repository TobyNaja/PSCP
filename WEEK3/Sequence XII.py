"""Sequence XII"""
def main():
    """Sequence XII"""
    n = int(input(""))
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            value = n - abs(i - j)
            row.append(f"{value:02}")
        row += row[-2::-1]
        print(" ".join(row))
    for i in range(n-1, 0, -1):
        row = []
        for j in range(1, n + 1):
            value = n - abs(i - j)
            row.append(f"{value:02}")
        row += row[-2::-1]
        print(" ".join(row))
main()
