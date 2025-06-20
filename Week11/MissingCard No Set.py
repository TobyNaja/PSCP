"""MissingCard No Set"""
def main():
    """dd"""
    suits = ['S', 'H', 'C', 'D']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    full_deck = [rank + suit for suit in suits for rank in ranks]
    remaining_cards = []
    for _ in range(51):
        x = input()
        remaining_cards.append(x)
    for card in full_deck:
        if card not in remaining_cards:
            missing_card = card
            break
    print(missing_card)
main()
