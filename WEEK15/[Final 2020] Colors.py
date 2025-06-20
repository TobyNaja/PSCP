"""[Final 2020] Colors"""
def main():
    """[Final 2020] Colors"""
    mylist = ["Red","Yellow","Blue"]
    color1 = input()
    color2 = input()
    if color1 not in mylist or color2 not in mylist:
        print("Error")
    elif color1 == color2:
        print(color2)
    elif color1 in ("Red", "Yellow") and color2 in ("Red", "Yellow"):
        print("Orange")
    elif color1 in ("Red", "Blue") and color2 in ("Red", "Blue"):
        print("Violet")
    elif color1 in ("Blue", "Yellow") and color2 in ("Blue", "Yellow"):
        print("Green")
main()
