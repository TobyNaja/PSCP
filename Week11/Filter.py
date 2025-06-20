"""Filter"""
import json
def main():
    """Filter"""
    data = {}
    x = input()
    score = float(input())
    a = json.loads(x)
    for i,j in a.items():
        if j >= score:
            data[i] = j
    if not data:
        print("Nope")
    else:
        for k,m in sorted(data.items()):
            print(f"{k}\t{m:.2f}")
main()
