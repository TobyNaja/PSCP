"""Stuttering"""
def main():
    """Stuttering"""
    txt = input().split()
    new = ""+txt[0]+" "
    x = len(txt)
    for i in range(1,x):
        if txt[i-1] == txt[i]:
            pass
        else:
            new += txt[i]+" "
    print(new.strip())
main()
