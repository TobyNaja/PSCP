"""Socks"""
def main():
    """Socks"""
    txt = input()
    mysock = []
    num = 0
    text = ""
    for i in txt:
        if i in text:
            pass
        else:
            text += i
            a = txt.count(i) // 2
            num += a
            for _ in range(a):
                mysock.append(i+i)
            mysock.sort()
    if mysock == []:
        print("None")
        print(0)
    else:
        for i in mysock:
            print(i,end=" ")
        print()
        print(num)
main()
