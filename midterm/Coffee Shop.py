"""Coffee Shop"""
def main():
    """Coffee Shop"""
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = int(input())
    pricea = e*a
    priceb = e*a
    if a > 1:
        pricea = a + ((e-1)*a)-((e-1)*a*b/100)
    if e*a <= d:
        priceb = (e*a)-((e*a)*(c/100))
    if pricea < priceb:
        print("1")
        print(f"{pricea:.2f}")
    elif pricea > priceb:
        print("2")
        print(f"{priceb:.2f}")
    else:
        print("2")
        print(f"{priceb:.2f}")
main()
