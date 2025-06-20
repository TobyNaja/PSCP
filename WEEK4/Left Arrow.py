"""Left Arrow"""
def main():
    """Left Arrow"""
    z = int(input())
    x = int(input())
    x = int((x-1)/2)
    b = x
    for _ in range(x):
        print(" "*x+"*"*z)
        x -= 1
    print("*"*z)
    for j in range(1, b+1):
        print(" "*j+"*"*z)
main()
