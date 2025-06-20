"""BadKeyboard"""
def main():
    """main"""
    txt = input()
    new_txt = ""
    for i in txt:
        if i == "i":
            new_txt += "o"
        elif i == "o":
            new_txt += "i"
        elif i == "I":
            new_txt += "O"
        elif i == "O":
            new_txt += "I"
        else:
            new_txt += i
    print(new_txt)
main()