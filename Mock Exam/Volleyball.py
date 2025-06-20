"""Volleyball"""
def main():
    """Volleyball"""
    txt = input()
    a = 0
    b = 0
    win_a = 0
    win_b = 0
    set_ = 0
    for i in txt:
        if i == "A":
            a += 1
        elif i == "B":
            b += 1
        if a >= 25 and a-b >= 2:
            win_a += 1
            set_ += 1
            print(f"Set {set_}: A ({a}) | B ({b})")
            a = 0
            b = 0
        elif b >= 25 and b-a >= 2:
            win_b += 1
            set_ += 1
            print(f"Set {set_}: A ({a}) | B ({b})")
            a = 0
            b = 0
        if set_ >= 4:
            if a >= 15 and a-b >= 2:
                win_a += 1
                set_ += 1
                print(f"Set {set_}: A ({a}) | B ({b})")
                a = 0
                b = 0
            elif b >= 15 and b-a >= 2:
                win_b += 1
                set_ += 1
                print(f"Set {set_}: A ({a}) | B ({b})")
        if win_a >= 3 or win_b >= 3:
            break
    if win_a >= 3:
        print(f"A won {win_a}:{win_b} set")
    elif win_b >= 3:
        print(f"B won {win_b}:{win_a} set")
    else:
        set_ += 1
        print(f"Set {set_}: A ({a}) | B ({b})")
        print("The game has not finished yet.")
main()
