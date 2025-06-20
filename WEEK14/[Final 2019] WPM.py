"""[Final 2019] WPM"""
def main(old, wpm):
    """[Final 2019] WPM"""
    if old == "Kids":
        if wpm < 11:
            print("Very Slow")
        elif 11 <= wpm <= 20:
            print("Slow")
        elif 21 <= wpm <= 30:
            print("Average")
        elif 31 <= wpm <= 40:
            print("Fast")
        elif wpm > 40:
            print("Very Fast")
    elif old == "Adults":
        if wpm < 26:
            print("Very Slow")
        elif 26 <= wpm <= 35:
            print("Slow/Beginner")
        elif 36 <= wpm <= 45:
            print("Intermediate/Average")
        elif 46 <= wpm <= 65:
            print("Fast/Advanced")
        elif 66 <= wpm <= 80:
            print("Very Fast")
        elif wpm > 80:
            print("Insane")
main(input(), int(input()))
