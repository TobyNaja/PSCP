"""d"""
def main():
    """d"""
    a = int(input())
    b = int(input())
    goal = int(input())
    if a+(b*5) >= goal:
        x = goal//5
        if x <= b:
            brick_small = goal-(x*5)
            if brick_small > a:
                print(-1)
            else:
                print(brick_small)
        elif x > b:
            brick_small = goal-(b*5)
            print(brick_small)
    else:
        print("-1")
main()
