"""Kabata"""
def main(num):
    """Kabata"""
    for _ in range(num):
        txt = input()
        if "ka"in txt and "ba" in txt and "ta" in txt:
            print("yes")
        else:
            print("no")
main(int(input()))
