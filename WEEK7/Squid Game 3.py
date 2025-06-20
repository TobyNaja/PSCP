"""Squid Game 3"""
def main():
    """Squid Game 3"""
    a = 0
    b = 0
    for _ in range(10):
        force = int(input())
        a += force
    for _ in range(10):
        force = int(input())
        b += force
    if a > b:
        print("B")
    elif a < b:
        print("A")
    else:
        print("AB")
main()
