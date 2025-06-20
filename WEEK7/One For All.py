"""One For All"""
def main(num):
    """One For All"""
    x = ""
    for i in range(1,num+1):
        name = input()
        if i == num:
            x += name+"_"+str(i)
        elif i%2:
            x +=name+("*"*i)
        elif not i%2:
            x += name+("-"*i)
    print(x)
main(int(input()))
