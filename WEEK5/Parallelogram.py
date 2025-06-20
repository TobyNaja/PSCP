"""Parallelogram"""
def main():
    """Parallelogram"""
    text = input()
    n = len(text)
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        print(spaces + text[:i+1])
    for i in range(1, n):
        print(text[i:])
main()
