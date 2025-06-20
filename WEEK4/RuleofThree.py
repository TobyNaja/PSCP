"""RuleofThree"""
def main():
    """RuleofThree"""
    x = int(input())
    best_price = 0
    best_weight = 0
    best_wp = 0
    for _ in range(x):
        price = float(input())
        weight = float(input())
        wp = weight/price
        if (wp > best_wp) or (wp == best_wp and price < best_price):
            best_wp = wp
            best_price = price
            best_weight = weight
    print(f"{best_price:.2f} {best_weight:.2f}")
main()
