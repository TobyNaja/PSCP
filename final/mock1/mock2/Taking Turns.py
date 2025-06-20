"""d"""
import json
def main():
    """d"""
    x = json.loads(input())
    new = []
    left, right = 0,len(x)-1
    new.append(x[right])
    right -= 1
    while left < right:
        for _ in range(2):
           new.append(x[left])
           left += 1
        for _ in range(2):
            new.append(x[right])
            right -=1
    print(new)
main()