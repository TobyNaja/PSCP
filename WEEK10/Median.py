"""Median"""
def main(num):
    """Median"""
    my_list = []
    for _ in range(num):
        x = float(input())
        my_list.append(x)
        my_list.sort()
    median = (num+1)/2
    if num % 2:
        ans = my_list[int(median-1)]
    else:
        a = my_list[int(median-1)]
        b = my_list[int(median)]
        ans = (a+b)/2
    print(f"{ans:.3f}")
main(int(input()))
