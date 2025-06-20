"""MissingCard"""
def main():
    """MissingCard"""
    suits = ['S', 'H', 'C', 'D']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    full_deck = {rank + suit for suit in suits for rank in ranks}
    remaining_cards = set()
    for _ in range(51):
        remaining_cards.add(input())
    ans = full_deck-remaining_cards
    for i in ans:
        print(i)
main()
