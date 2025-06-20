"""bill"""
def main():
    """bill"""
    price = int(input())
    service = price*(10/100)
    if service <= 50:
        service = 50
    elif service >= 1000:
        service = 1000
    price = price + service
    vat = price*(7/100)
    price += vat
    print(f"{price:.2f}")
main()
