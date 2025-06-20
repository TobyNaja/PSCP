"""[Final 2020] Area"""
def main(num):
    """[Final 2020] Area"""
    count = 0
    for _ in range(num):
        x = input().replace(" ", "")
        count += len(x)
    print(count)
main(int(input()))
