"""Debaratna Road"""
def main():
    """Debaratna Road"""
    kilo = float(input())
    if 0 <= kilo <= 5.032:
        print("Bangkok")
    elif 5.032 < kilo <= 35.477:
        print("Samut Prakarn")
    elif 35.477 < kilo <= 52.900:
        print("Chachoengsao")
    elif 52.900 < kilo <= 58.855:
        print("Chon Buri")
    else:
        print("InValid")
main()
