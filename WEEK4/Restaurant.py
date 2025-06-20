"""Restaurant"""
def main():
    """Restaurant"""
    price = float(input())
    pro = float(input())
    per = float(input())
    menu = float(input())
    total = (price+menu)-((price+menu)*(per/100))
    if price >= pro:
        price = price-(price*(per/100))
    if 0 < per <= 100:
        if total > price:
            print(f"No {total-price:.3f}")
        elif total == price:
            print("Yes")
        else:
            print(f"Yes {price-total:.3f}")
    else:
        print("Yes")
main()
