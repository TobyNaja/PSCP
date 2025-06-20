"""Pre"""
def main():
    """d"""
    x = int(input())
    y = int(input())
    d = int((y-1)/2)
    up = d
    down = 0
    for _ in range(d):
        print(" "*(up-1),"*"*x)
        up -= 1
    print("*" * x)
    for _ in range(d):
        print(" "*(down),"*"*x)
        down += 1
main()
