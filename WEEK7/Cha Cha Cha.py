"""Cha Cha Cha"""
import math
def main():
    """Cha Cha Cha"""
    num = int(input())
    money = 0
    for _ in range(num):
        x = math.ceil(float(input()))
        money += x*8720
    print(money)
main()
