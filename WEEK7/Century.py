"""Century"""
import math
def main():
    """Century"""
    num = int(input())
    for _ in range(num):
        century = input()
        if century[:4] == "B.E." and int(century[5:]) > 543:
            year = int(century[5:])-543
            year = math.ceil(year/100)
        elif century[:4] == "A.D.":
            year = int(century[5:])
            year = math.ceil(year/100)
        else:
            year = "ERROR"
        print(year)
main()
