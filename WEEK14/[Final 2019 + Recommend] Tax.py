"""[Final 2019 + Recommend] Tax"""
def main():
    """[Final 2019 + Recommend] Tax"""
    year = int(input())
    cc = int(input())
    money = 0
    if 1 <= cc <= 600:
        money += cc * 0.5
    elif 601 <= cc <= 1800:
        money += (cc-600)*1.5 + 300
    elif 1800 < cc:
        money += (cc-1800)*4 + 1800 + 300
    if year == 6:
        money = money-(money*0.1)
    elif year == 7:
        money = money-(money*0.2)
    elif year == 8:
        money = money-(money*0.3)
    elif year == 9:
        money = money-(money*0.4)
    elif year >= 10:
        money = money-(money*0.5)
    print(f"{money:.02f}")
main()
