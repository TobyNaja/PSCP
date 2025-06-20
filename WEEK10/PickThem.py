"""PickThem"""
import json
def main():
    """PickThem"""
    x = input()
    d = 0
    my_list = json.loads(x)
    for i in my_list:
        if not int(i) % 2:
            print(i)
            d += 1
    if not d:
        print("Nope")
main()
