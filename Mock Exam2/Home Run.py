"""Home Run"""
def main(num):
    """Home Run"""
    homerun = float(input())
    count = 0
    for _ in range(num):
        stadium = float(input())
        if homerun > stadium:
            count += 1
    print(count)
main(int(input()))
