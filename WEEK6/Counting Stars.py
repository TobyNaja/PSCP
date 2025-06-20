"""Counting Stars"""
def main():
    """Counting Stars"""
    stars = input()
    comet = 0
    shooting_star = 0
    constellation = 0
    x = ""
    for i, _ in enumerate(stars):
        if stars[i] == " ":
            x = ""
        else:
            x += stars[i]
        if x in("~*","*~"):
            comet += 1
            x = ""
        elif x == "*/":
            shooting_star += 1
            x = ""
        elif x == "**":
            constellation += 1
            x = ""
        if len(x) >= 2:
            x = stars[i]
    if constellation > 0 or comet > 0 or shooting_star >0:
        print(f"constellation: {constellation}")
        print(f"comet: {comet}")
        print(f"shooting star: {shooting_star}")
    else:
        print("Tonight is a quiet night.")
main()
