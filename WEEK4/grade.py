"""Sequence III"""
import math
def main():
    """Sequence III"""
    num = int(input())
    count = 0
    score = 0
    for _ in range(num):
        x = float(input())
        if 0 <= x < 60:
            score = 0
        elif 60 <= x < 65:
            score = 0.5
        elif 65 <= x < 70:
            score = 1
        elif 70 <= x < 75:
            score = 1.5
        elif 75 <= x < 80:
            score = 2.0
        elif 80 <= x < 85:
            score = 2.5
        elif 85 <= x < 90:
            score = 3
        elif 90 <= x < 95:
            score = 3.5
        elif 95 <= x <= 100:
            score = 4
        count += score
    ans = count/num
    ans = math.floor(ans * 100) / 100
    print(f"{ans:.2f}")
main()
