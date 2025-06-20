"""Fever"""
def main():
    """Fever"""
    t = float(input())
    if 36 <= t < 38:
        print("No Fever")
    elif 38 <= t < 39:
        print("Mild Fever")
    elif 39 <= t < 40:
        print("High Fever")
    elif 40 <= t:
        print("Very High Fever")
main()
