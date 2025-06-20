"""Backward"""
def main():
    """Backward"""
    my_list = []
    while True:
        txt = input()
        if txt == "NULL":
            break
        my_list.append(txt)
    my_list.reverse()
    for i in my_list:
        print(i)
main()
