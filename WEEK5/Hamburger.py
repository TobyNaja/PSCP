'''Hamburger'''
def main():
    '''Variable'''
    left = int(input())
    right = int(input())
    beef = (left+right)*2
    print(("|"*left)+("*"*beef)+("|"*right))
main()
