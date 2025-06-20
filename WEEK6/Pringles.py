"""Pringles"""
def main():
    """Pringles"""
    top = input()
    mid = input()
    under = input()
    num = int(input())
    count = 0
    txt = ""
    for i in mid:
        if num > 0 and i == ")":
            count += 1
            txt += " "
        else:
            txt += i
        num -= 1
    print(count)
    if txt.count(")") > 0:
        print("There are still some left.")
    else:
        print("None.")
    print(top)
    print(txt)
    print(under)
main()
