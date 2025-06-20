"""diamond"""
def main():
    """Diamond Shape"""
    x = int(input())
    for i in range(x // 2):
        for j in range(x):
            if j in (x // 2 - i, x // 2 + i):
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print("*" * x)
    for i in range(x // 2 - 1, -1, -1):
        for j in range(x):
            if j in (x // 2 - i, x // 2 + i):
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()
