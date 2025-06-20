"""d"""
def main():
    """d"""
    summ = float(input())
    most = float(input())
    x = most-max(0, summ-2*most)
    if x > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
