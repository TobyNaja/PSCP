"""BTSMRT"""
def main():
    """BTSMRT"""
    day = input()
    old = float(input())
    hight = float(input())
    if (day == "Children Day" and old < 14 and hight <= 140) or (old < 14 and hight < 90):
        print("FREE")
    elif day == "Senior Day" and old >= 60:
        print("FREE")
    else:
        print("PAY")
main()
