"""LineSorting"""
def main(num):
    """LineSorting"""
    my_list = []
    for _ in range(num):
        txt = input()
        my_list.append(txt)
    my_list = sorted(my_list, key=len)
    for i in my_list:
        print(i)
main(int(input()))
