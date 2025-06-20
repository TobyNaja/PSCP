"""Stair"""
def main():
    """Stair"""
    y = int(input())
    num = int(input())
    count = 0
    stair = 0
    no = False
    for j in range(num):
        x = int(input())
        if x <= y:
            stair += x
            if stair == y:
                count += 1
                stair = 0
            elif stair > y:
                count += 1
                stair = x
                if j == num-1 and stair <= y:
                    count += 1
            elif stair < y and j == num-1:
                count += 1
        elif x > y:
            no = True
    if no:
        print("NO")
    else:
        print(count)
main()
