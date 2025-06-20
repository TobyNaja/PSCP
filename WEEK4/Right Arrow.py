"""RIGHT Arrow"""
def main():
    """RIGHT Arrow"""
    z = int(input())
    x = int(input())
    x = int((x-1)/2)
    b = x
    for j in range(0, b):
        print(" "*j+"*"*z)
    print(" "*(b)+"*"*z)
    for _ in range(x):
        print(" "*(x-1)+"*"*z)
        x -= 1
main()
