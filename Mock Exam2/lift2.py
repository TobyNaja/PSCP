"""Lift"""
def main(num):
    """Lift"""
    lift = float(input())
    total = 0
    result = False
    for _ in range(num):
        old = int(input())
        weight = float(input())
        total += weight
        if old >= 12:
            result = True
    if total > lift or not result:
        print("Not Safe")
    else:
        print("Safe")
main(int(input()))
