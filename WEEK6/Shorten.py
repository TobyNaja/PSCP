"""Shorten"""
def main():
    """Shorten"""
    num = ""
    count = 0
    start = False
    start_num = None
    while True:
        number = int(input())
        if number == -1:
            break
        if start_num is None:
            start_num = number
            num += str(number)
        elif number-count == 1:
            start = True
        else:
            if start:
                num += f"-{count}"
            num += f", {number}"
            start = False
        count = number
    if start:
        num += f"-{count}"
    print(num)
main()
