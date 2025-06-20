"""d"""
def main():
    """d"""
    a = float(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = float(input())
    caps = 0
    bottles = 0
    total_bottles = 0
    while f >= a:
        f -= a
        bottles += 1
        caps += 1
        total_bottles += 1
        while caps >= b or bottles >= d:
            while caps >= b:
                total_bottles += c
                caps = caps - b + c
                bottles += c
            while bottles >= d:
                total_bottles += e
                bottles = bottles - d + e
                caps += e
    print(total_bottles)
main()
