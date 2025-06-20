"""IT Business"""
def main(bank, money):
    """IT Business"""
    error = 0
    while True:
        x = input()
        if "D" in x and float(x[2:]) <= money:
            bank += float(x[2:])
            money -= float(x[2:])
            error = 0
        elif "W" in x and float(x[2:]) <= bank:
            money += float(x[2:])
            bank -= float(x[2:])
            error = 0
        else:
            error += 1
        if x == "end" or error >= 3:
            break
    print(f"{bank:.2f}")
    print(f"{money:.2f}")
main(float(input()),float(input()))
