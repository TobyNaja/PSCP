"""Water"""
def main(num):
    """Water"""
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    water = 0
    for _ in range(num):
        waterper = 0
        x = float(input())
        if x > b:
            waterper += (b*a)+((x-b)*c)
        else:
            waterper += x*a
        if waterper <= d:
            waterper = 0
        water += waterper
    print(f"{water:.2f}")
main(int(input()))
