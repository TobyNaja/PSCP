"""d"""
def main():
    """d"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    pro = b+c
    if pro <= d:
        count = d//pro
        if not count:
            price = count*b*a
            donut = count*(b+c)
        else:
            countt = d%pro
            if countt >= b:
                price = (count*b*a)+(b*a)
                donut = count*(b+c)+countt+c
            else:
                price = (count*b*a)+(countt*a)
                donut = count*(b+c)+countt
    else:
        donut = d
        price = d*a
    print(price,donut)
main()
