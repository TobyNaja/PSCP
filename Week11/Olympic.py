"""w"""
def main():
    """w"""
    n = int(input())
    dicts = {}
    for _ in range(n):
        user = input().split()
        gold = int(user[1])
        silver = int(user[2])
        bronze = int(user[3])
        dicts[user[0]] = [gold, silver, bronze, gold+silver+bronze]
    sorte = sorted(dicts.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2], x[0]))
    num = 0
    num_o = 0
    previous_val_tuple = None
    for key, val in sorte:
        val_tuple = tuple(val)
        num_o += 1
        if val_tuple != previous_val_tuple:
            num = num_o
            previous_val_tuple = val_tuple
        print(num, key, *val)
main()
