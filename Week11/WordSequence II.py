"""WordSequence II"""
def main(text1, text2):
    """WordSequence II"""
    ans = ""
    length = max(len(text1), len(text2))
    if len(text1) < len(text2):
        for i in range(length + 1):
            ans = text2[:i] + text1[i:]
            print(ans)
    else:
        for i in range(len(text1)+1):
            ans= text2[:i] + text1[i:]
            print(ans)
main(input(), input())
