"""RockPaperScissor"""
def main():
    """RockPaperScissor"""
    a_score = 0
    b_score = 0
    x = input()
    for i in range(0, len(x), 2):
        a = x[i]
        b = x[i+1]
        if a == 'R' and b == 'S':
            a_score += 1
        elif a == 'S' and b == 'P':
            a_score += 1
        elif a == 'P' and b == 'R':
            a_score += 1
        elif b == 'R' and a == 'S':
            b_score += 1
        elif b == 'S' and a == 'P':
            b_score += 1
        elif b == 'P' and a == 'R':
            b_score += 1
    if a_score > b_score:
        print(f"A win {a_score}-{b_score}")
    elif b_score > a_score:
        print(f"B win {b_score}-{a_score}")
    else:
        print(f"DRAW {a_score}")
main()
