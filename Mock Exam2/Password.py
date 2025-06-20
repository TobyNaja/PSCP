"""Password"""
import math
def main():
    """Password"""
    password = input()
    r = 0
    decimal = False
    islower = False
    isupper = False
    isprintable = False
    l = len(password)
    for i in password:
        if i.isdecimal() and not decimal:
            r += 10
            decimal = True
        elif i.islower() and not islower:
            r += 26
            islower = True
        elif i.isupper() and not isupper:
            r += 26
            isupper = True
        elif not i.isnumeric() and not i.isalpha() and not isprintable:
            r += 32
            isprintable = True
    ans = math.floor(math.log(r**l,2))
    print(ans)
    if ans < 28:
        print("Very Weak")
    elif 28 <= ans <= 35:
        print("Weak")
    elif 36 <= ans <= 59:
        print("Reasonable")
    elif 60 <= ans <= 127:
        print("Strong")
    elif ans >= 128:
        print("Very Strong")
main()
