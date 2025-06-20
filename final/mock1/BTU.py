"""BTU"""
def main():
    """BTU"""
    area = int(input())
    hight = int(input())
    people = int(input())
    room = input()
    x = input()
    if 100 <= area <= 550:
        d = btu_1(area)
    else:
        d = btu_2(area)
    if hight > 8:
        d += (hight - 8)*1000
    if people > 2:
        d += (people-2) * 600
    if room == "kitchen":
        d += 4000
    if x == "facing the sun":
        d += d*0.1
    elif x == "shaded":
        d -= d*0.1
    print(int(d))
def btu_1(area):
    """d"""
    if 100 <= area <= 150:
        return 5000
    elif 151 <= area <= 250:
        return 6000
    elif 251 <= area <= 300:
        return 7000
    elif 301 <= area <= 350:
        return 8000
    elif 351 <= area <= 400:
        return 9000
    elif 401 <= area <= 450:
        return 10000
    elif 451 <= area <= 550:
        return 12000

def btu_2(area):
    """d"""
    if 551 <= area <= 700:
        return 14000
    elif 701 <= area <= 1000:
        return 18000
    elif 1001 <= area <= 1200:
        return 21000
    elif 1201 <= area <= 1400:
        return 23000
    elif 1401 <= area <= 1500:
        return 24000
    elif 1501 <= area <= 2000:
        return 30000
    elif 2001 <= area <= 2500:
        return 34000
main()