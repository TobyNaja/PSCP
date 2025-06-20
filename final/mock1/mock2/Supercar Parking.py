"""[Mock Final 2023] Supercar Parking"""
def main():
    """[Mock Final 2023] Supercar Parking"""
    x = input()
    a = x + " "
    count = 0
    supercar = 0
    if x[0] == "0":
        count = 1
    for i in range(len(x)):
        if a[i] == "1":
            count = 0
        elif a[i] == "0":
            count += 1
            if count == 2 and a[i+1] in ("0"," "):
                supercar += 1
                count = 0
    print(supercar)
main()
