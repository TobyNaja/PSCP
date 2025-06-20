"""Phone number"""
def main() :
    """Phone number"""
    num = input()
    inout = input()
    long = len(num)
    if inout == "Domestic" :
        if long == 10 :
            group1 = num[0:2]
            group2 = num[2:6]
            group3 = num[6:11]
            print(f"{group1} {group2} {group3}")
        if long == 9 :
            group1 = num[0:1]
            group2 = num[1:5]
            group3 = num[5:10]
            print(f"{group1} {group2} {group3}")
    elif inout == "International" :
        if long == 10 :
            group1 = num[1:2]
            group2 = num[2:6]
            group3 = num[6:11]
            print(f"+66{group1} {group2} {group3}")
        if long == 9 :
            group2 = num[1:5]
            group3 = num[5:10]
            print(f"+66 {group2} {group3}")
main()
