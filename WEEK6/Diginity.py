"""Diginity"""
def main():
    """Diginity"""
    while True:
        num = str(int(input()))
        if num == "0":
            break
        count = 0
        if len(num) <= 1 :
            print(num)
        else:
            while len(num) > 1:
                for i in num:
                    count += int(i)
                num = str(count)
                if len(num) <= 1:
                    break
                count = 0
            print(count)
main()
