"""ChristmasTree"""
def main():
    """ChristmasTree"""
    x = int(input())
    b = int(input())
    u = x-1
    for i in range(1, (x*2) + 1, 2):
        print(" " * u + "*" * i)
        u -= 1
    c = x-2
    for _ in range(b):
        print(" " * c + "-" * 3)
main()
