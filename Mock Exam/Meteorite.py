"""Meteorite"""
def main(a,b,c):
    """Meteorite"""
    count = 0
    shoot = 0
    while a >= c:
        a /= b
        shoot += b**count
        count += 1
    print(shoot)
main(float(input()), int(input()),float(input()))
