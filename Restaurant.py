"""d"""
import json
def main():
    """d"""
    x = json.loads(input())
    flatten = []
    def flat(l):
        for i in l:
            if isinstance(i, list):
                flat(i)
            else:
                flatten.append(i)
    flat(x)
    flatten.sort(reverse=True)
    print(flatten)
main()
