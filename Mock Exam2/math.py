"""Niwarn World"""
import math
def x(n):
    """Find function x"""
    ans = 2+((math.log((n**2),2))/((2*n)*(math.log(n,2))))
    return ans
def y(n,s):
    """Find function y"""
    ans = ((math.sin(math.radians(30)))+math.sqrt(2*s))/(x(n) +3)
    return ans
def z(k):
    """Find function k"""
    ans = ((y(k,k))**2) + ((8456*((x(k))**4))/(24*k))
    return ans
def main():
    """Niwarn World"""
    n = float(input())
    s = float(input())
    k = float(input())
    ans1 = x(n)
    ans2 = y(n,s)
    ans3 = z(k)
    print(f"X: {ans1:.1f}, Y: {ans2:.1f}, Z: {ans3:.1f}")
main()