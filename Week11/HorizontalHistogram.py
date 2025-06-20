"""Easy Histogram"""
def main():
    """F"""
    text = input().strip()
    index = {}
    ans = {}
    bull = ''
    for i in text :
        if i.isalpha():
            if i in index:
                index[i] += 1
            else:
                index[i] = 1
    ans = sorted(index.items(), key = lambda x: (x[0].isupper() , x[0].lower()))
    for char , num in ans:
        bull = '-' * num
        five = '|'.join([bull[i:i+5] for i in range(0 , len(bull) ,5)])
        print(f"{char} : {five}")
main()
