"""Seeker"""
def main():
    """Seeker"""
    txt = input()
    ans = ""
    count = 0
    a = []
    for i in txt:
        st = True
        if i.isdecimal() and st:
            ans += i
            st = True
        else:
            st = False
            if ans.isdecimal():
                a.append(ans)
            ans = ""
    if ans.isdecimal():
        a.append(ans)
    for i in a:
        count += int(i)
    print(count)
main()
