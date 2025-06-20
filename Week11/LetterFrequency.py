"""LetterFrequency"""
def main():
    """LetterFrequency"""
    count = 0
    ans = ""
    txt = input().replace(" ","")
    words = dict.fromkeys(txt,0)
    for i in txt:
        words[i] += 1
    for i,j in words.items():
        if int(j) >= count:
            ans = i
            count = j
    print(ans)
main()
