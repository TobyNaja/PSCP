"""Turnstile"""
def main():
    """Turnstile"""
    lock = False
    count = 0
    while True:
        x = input()
        if x == "END":
            break
        if x == "P":
            if lock:
                count += 1
                lock = False
        elif x == "C":
            lock = True
    print(count)
main()
