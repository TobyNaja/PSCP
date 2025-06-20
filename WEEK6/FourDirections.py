"""FourDirections"""
def main():
    """FourDirections"""
    x = input()
    line1 = []
    line2 = []
    line3 = []
    line4 = []
    line5 = []
    for i in x:
        if i == "U":
            line1.append("  *  ")
            line2.append(" *** ")
            line3.append("* * *")
            line4.append("  *  ")
            line5.append("  *  ")
        elif i == "D":
            line1.append("  *  ")
            line2.append("  *  ")
            line3.append("* * *")
            line4.append(" *** ")
            line5.append("  *  ")
        elif i == "L":
            line1.append("  *  ")
            line2.append(" *   ")
            line3.append("*****")
            line4.append(" *   ")
            line5.append("  *  ")
        elif i == "R":
            line1.append("  *  ")
            line2.append("   * ")
            line3.append("*****")
            line4.append("   * ")
            line5.append("  *  ")
    print(" ".join(line1))
    print(" ".join(line2))
    print(" ".join(line3))
    print(" ".join(line4))
    print(" ".join(line5))
main()
