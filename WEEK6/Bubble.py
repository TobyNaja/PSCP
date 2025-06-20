"""Bubble"""
def main():
    """Bubble"""
    bubble = input()
    jump = 0
    skip = 0
    for i in range(len(bubble)):
        if skip > 0:
            skip -= 1
            continue
        if bubble[i] == "|":
            ans = "POSSIBLE"
        elif bubble[i] == "^" and bubble[i+1] == " ":
            ans = "IMPOSSIBLE"
        elif bubble[i] == "o" and bubble[i+1] == " ":
            ans = "IMPOSSIBLE"
        elif bubble[i] == "O" and (bubble[i+2] == " " or bubble[i+1] == " "):
            ans = "IMPOSSIBLE"
        elif bubble[i] == "O" and (bubble[i+2] != " " or bubble[i+1] in("|","o","O")):
            skip += 2
            jump += 1
        else:
            jump += 1
            ans = "POSSIBLE"
        if ans == "IMPOSSIBLE":
            dis = len(bubble[i+1:])
            break
    print(ans)
    if ans == "POSSIBLE":
        print(jump)
    else:
        print(dis)
main()
