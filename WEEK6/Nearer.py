"""Nearer"""
def main():
    """Nearer"""
    alice = int(input())
    bob = int(input())
    ice = int(input())
    dis1 = abs(ice-alice)
    dis2 = abs(ice-bob)
    if dis1 < dis2:
        print("Alice",dis1)
    elif dis2 < dis1:
        print("Bob",dis2)
    else:
        print("Sundaes",dis1)
main()
