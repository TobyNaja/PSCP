"""milk"""
def main():
    """milk"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    count = 0
    far = 0
    if a*b <= d and b:
        result = d//(a*b)
        count += (result*b) + (result*c)
        far +=  (result*b) + (result*c)
        if d%(a*b):
            result = d%(a*b)//a
            count += result
            far += result
        while far >= b:
            count += c
            far += c-b
    else:
        result = d//a
        count += result
    print(count)
main()
