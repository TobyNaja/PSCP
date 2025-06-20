"""Stamps"""
def main(n):
    """Stamps"""
    stamp = 0
    all_price = 0
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    for _ in range(n):
        price = int(input())
        if price >= a:
            stamp += b
        while stamp >= c and price >= 0:
            stamp -= c
            price -= d
        all_price += price
    print(all_price)
main(int(input()))
