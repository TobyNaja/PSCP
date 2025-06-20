"""PickThem"""
def main():
    """PickThem"""
    d = 0
    x = input()
    my_list = list(map(int, x.split()))
    my_list.reverse()
    for i in my_list:
        if not int(i) % 3 or not int(i) % 5:
            print(i)
            d += 1
    if not d:
        print("Nope")
main()
