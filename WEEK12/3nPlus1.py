"""3nPlus1"""
def main():
    """3nPlus1"""
    my_list= []
    while True:
        x = int(input())
        if not x:
            break
        my_list.append(x)
    for i in my_list:
        count = 0
        while True:
            count += 1
            if i == 1:
                break
            if not i%2:
                i /= 2
            else:
                i = (i*3)+1
        print(count)
main()
