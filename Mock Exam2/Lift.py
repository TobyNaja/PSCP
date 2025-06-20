"""Lift"""
def main(num):
    """Lift"""
    lift = float(input())
    total = 0
    result = False
    child = False
    for _ in range(num):
        old = int(input())
        weight = float(input())
        total += weight
        if old >= 12:
            result = True
        else:
            child = True
    if total > lift:
        print("Not Safe")
    elif not result and child:
        print("Not Safe")
    else:
        print("Safe")
main(int(input()))
