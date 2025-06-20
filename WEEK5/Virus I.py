"""Virus I"""
def main():
    """Virus I"""
    virus = input()
    count = 0
    for i in virus:
        if i.islower():
            count += 1
        else:
            pass
    print(count)
main()
