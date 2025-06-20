"""Ball"""
def main():
    """ball"""
    height = float(input())
    count = 0
    while True:
        if height < 0.01:
            break
        height = height*(3/5)
        count += 1
    print(count-1)
main()
