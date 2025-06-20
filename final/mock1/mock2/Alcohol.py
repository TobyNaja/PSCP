"""Alcohol"""
def main():
    """Alcohol"""
    sex = input()
    weight = float(input())
    ls = input()
    vpk = float(input())
    vpa = float(input())
    num = int(input())
    hours = int(input())
    vpd = (vpa*vpk/100)*num
    if sex == "Male":
        x = vpd/(weight*0.68*10)
    elif sex == "Female":
        x = vpd/(weight*0.55*10)
    for _ in range(hours):
        x -= 0.015
    if ls == "No" or x > 0.05:
        print("Not Safe")
    else:
        print("Safe")
main()
