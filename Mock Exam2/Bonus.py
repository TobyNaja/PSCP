"""bonus"""
def main():
    """bonus"""
    money = int(input())
    year = int(input())
    month = int(input())
    if month >= 10:
        year += 1
    if year >= 20:
        year = 20
    bonus = money*year
    if bonus >= 1000000:
        bonus = 1000000
    elif bonus <= 5000:
        bonus = 5000
    print(bonus)
main()
