"""Heads and Legs"""
def main():
    """Heads and Legs"""
    heads = int(input())
    legs = int(input())
    rabbit = int((legs-(2*heads))/2)
    bird = heads-rabbit
    if legs % 2 or bird < 0 or rabbit < 0:
        print("Impossible")
    else:
        print(rabbit,bird)
main()
