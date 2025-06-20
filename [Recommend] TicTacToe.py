"""[Recommend] TicTacToe"""
def main():
    """[Recommend] TicTacToe"""
    x = list(input() for _ in range(3))
    for row in x:
        if row == "OOO":
            print("O WIN")
            return
        if row == "XXX":
            print("X WIN")
            return
    for i in range(3):
        if x[0][i] == x[1][i] == x[2][i] == "O":
            print("O WIN")
            return
        if x[0][i] == x[1][i] == x[2][i] == "X":
            print("X WIN")
            return
    if x[0][0] == x[1][1] == x[2][2] == 'O' or x[0][2] == x[1][1] == x[2][0] == 'O':
        print("O WIN")
    elif x[0][0] == x[1][1] == x[2][2] == 'X' or x[0][2] == x[1][1] == x[2][0] == 'X':
        print('X WIN')
    else:
        print('DRAW')
main()
