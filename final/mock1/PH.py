"""PH"""
def main():
    """PH"""
    ph = float(input())
    if 0 <= ph < 7:
        print("acidic")
    elif ph == 7:
        print("neutral")
    elif 7 < ph <= 14:
        print("akaline")
    else:
        print("error")
main()
