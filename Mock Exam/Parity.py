"""Parity"""
def main(bit,x):
    """Parity"""
    a = 0
    for i in bit:
        if i == "1":
            a += 1
    if not a%2 and x == "Even":
        print(bit+"0")
    elif not a%2 and x == "Odd":
        print(bit+"1")
    elif a%2 and x == "Even":
        print(bit+"1")
    elif a%2 and x == "Odd":
        print(bit+"0")
main(input(),input())
