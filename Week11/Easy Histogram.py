"""Easy Histogram"""
def main():
    """Main Function"""
    txt = input().replace(" ","")
    words = sorted(txt,key=lambda b: (b.lower(), b.isupper()))
    words = dict.fromkeys(words,0)
    for i in txt:
        words[i] += 1
    for i,j in words.items():
        print(i,"=",j)
main()
