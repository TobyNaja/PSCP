"""MissingNumber No Set"""
def main():
    """MissingNumber No Set"""
    num = int(input())
    list2 = []
    for _ in range(num):
        k = int(input())
        if not k:
            break
        list2.append(k)
        list2.sort()
    missing_numbers = []
    for i in range(1, num + 1):
        if i not in list2:
            missing_numbers.append(i)
    for missing in missing_numbers:
        print(missing)
main()
