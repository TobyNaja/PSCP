"""B - Fully pair?"""
def main():
    """Run Length Encoding with combined 'a' counts without using a set"""
    txt = input()
    new_txt = ""
    for i in txt:
        x = txt.count(i)
        if x % 2 and i not in new_txt:
            new_txt += i
    if not new_txt:
        new_txt += "fully paired"
    print(new_txt)
main()
