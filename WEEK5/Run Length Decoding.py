"""Run Length Encoding"""
def main():
    """Run Length Encoding"""
    txt = input()
    end_txt = ""
    count = ""
    for i in txt:
        if i.isdigit():
            count += i
        else:
            text = int(count)*i
            end_txt += text
            count = ""
    print(end_txt)
main()
