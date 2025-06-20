"""AndAgain"""
def main():
    """AndAgain"""
    # a e i o u
    x = input()
    sara = 0
    a = 0
    my_list = list(map(str, x.split()))
    for i in sorted(my_list):
        for j in i:
            if j in("a", "e", "i", "o", "u"):
                sara += 1
        if sara >= 2:
            ans = i.replace(".","")
            print(ans)
            a += 1
        sara = 0
    if a <= 0:
        print("Nope")
main()
