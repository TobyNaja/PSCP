"""Sequence N"""
def main():
    """Sequence N"""
    x = int(input())
    for j in range(x):
        for i in range(x):
            if not i or i == (x - 1)or i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()
