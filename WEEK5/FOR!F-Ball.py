"""FOR!F-Ball"""
def main():
    """FOR!F-Ball"""
    forball = input()
    position = 1
    for i in forball:
        if i == 'A':
            if position == 1:
                position = 2
            elif position == 2:
                position = 1
        elif i == 'B':
            if position == 2:
                position = 3
            elif position == 3:
                position = 2
        elif i == 'C':
            if position == 1:
                position = 3
            elif position == 3:
                position = 1
    print(position)
main()
