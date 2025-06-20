"""[Final 2019] Pro"""
def main():
    """[Final 2019] Pro"""
    x = float(input())
    y = float(input())
    a = int(input())
    z = int(input())
    if z >= x:
        count = z//x
        f = z%x
        money = int((count*y*a)+(f*a))
    else:
        money = int(z*a)
    print(money)
main()
