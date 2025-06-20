'''Key'''
def main():
    '''Variable'''
    key = input()
    count = 0
    for i in key:
        count += int(i)
    x = int(key[10:])
    x *= 10
    ans = count+x
    if ans<1000:
        print(ans+1000)
    else:
        ans2 = str(ans)[::-1]
        ans3 = str(ans2)[:4]
        print(str(ans3)[::-1])
main()
