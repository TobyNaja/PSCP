"""Calculator"""
def main(num):
    """Calculator"""
    txt = ""
    if num == 1:
        print("1")
    else:
        for i in range(1,num+1):
            txt += str(i)
        ans = len(txt)+num
        print(ans)
main(int(input()))
