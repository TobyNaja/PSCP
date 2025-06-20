"""Real"""
def main():
    """Real"""
    ans = ""
    for _ in range(3):
        a,b,c,d,e,f,g,dp = input(),input(),input(),input(),input(),input(),input(),input()
        if "off" in g and "on" in(a,b,c,d,e,f):
            ans += "0"
        elif "off" in(g,a,d,e,f)and "on" in(b,c):
            ans += "1"
        elif "off" in(f,c)and "on" in(b,a,d,e,g):
            ans += "2"
        elif "off" in(f,e)and "on" in(b,a,d,c,g):
            ans += "3"
        elif "off" in(a,e,d)and "on" in(b,f,c,g):
            ans += "4"
        elif "off" in(e,b)and "on" in(a,f,c,g,d):
            ans += "5"
        elif "off" in(b)and "on" in(a,f,c,g,d,e):
            ans += "6"
        elif "off" in(d,e,f,g)and "on" in(a,b,c):
            ans += "7"
        elif "on" in(a,b,c,d,e,f,g):
            ans += "8"
        elif "off" in(e) and "on" in(a,b,c,d,f,g):
            ans += "9"
        if dp == "on":
            ans += "."
    print(ans)
main()