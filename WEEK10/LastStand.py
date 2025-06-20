"""LastStand"""
import json
def main():
    """LastStand"""
    x = input()
    my_list = json.loads(x)
    for i in my_list:
        i = str(i)
        print(i[-1:])
main()
