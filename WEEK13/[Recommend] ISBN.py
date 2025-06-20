"""d"""
def main():
    """[Recommend] ISBN"""
    x = input().replace("-", "")
    if x[9] == 'X':
        d = 10
    else:
        d = int(x[9])
    count = 0
    g = 10
    for i in range(9):
        count += int(x[i]) * g
        g -= 1
    count = -count
    gg = count % 11
    if gg == d:
        print("Yes")
    else:
        if gg == 10:
            print("No X")
        else:
            print(f"No {gg}")
main()
