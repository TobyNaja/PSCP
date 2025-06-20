"""Helloooo"""
def main():
    """Helloooo"""
    txt = input()
    re = txt[::-1]
    check = True
    new = ""
    for i in re:
        if i in ("a", "e", "i", "o", "u") and check:
            new += i * 4
            check = False
        else:
            new += i
    print(new[::-1])
main()
