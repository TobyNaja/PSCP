'''Future Message'''
def main():
    '''Variable'''
    text = input()
    if text.isnumeric():
        print("Number")
    elif text.isupper():
        print("Uppercase")
    elif text.islower():
        print("Lowercase")
    elif text.istitle():
        print("Title")
    elif text.isspace():
        print("Space")
    else:
        print("Other")
main()
