"""d"""
def more(a,b):
    """d"""
    if a > b:
        return a
    return b
def main():
    """d"""
    most, mid = (input()), (input())
    last = input()
    c1 = int(most+mid+last)
    c2 = int(mid+most+last)
    c3 = int(last+mid+most)
    c4 = int(last+most+mid)
    c5 = int(most+last+mid)
    c6 = int(mid+last+most)
    print(more(more(more(more(more(c1,c2),c3),c4),c5),c6))
main()
