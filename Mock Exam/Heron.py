"""Heron"""
def main(a,b,c):
    """Heron"""
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print(f"{area:.3f}")
main(float(input()),float(input()),float(input()))
