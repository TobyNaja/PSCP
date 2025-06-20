"""Harshad"""
def main():
    """Harshad"""
    for _ in range(10):
        count = 0
        num = str(abs(int(input())))
        for i in num:
            count += int(i)
        if num == "0":
            print("No")
        elif not int(num) % int(count):
            print("Yes")
        else:
            print("No")
main()
