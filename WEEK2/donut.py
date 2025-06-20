"""Donut"""
def main():
    """Donut"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    box = b + c
    count = d // box
    scrap = d % box
    price = 0
    ber = 0
    if b < d:
        price += count * b * a
        ber += box * count
        if scrap >= b:
            price += b * a
            ber += box
        else:
            ber += scrap
            price += scrap * a
    else:
        if b == d:
            price += b * a
            ber += box
        elif b > d:
            price += d * a
            ber += d
    print(price, ber)
main()
